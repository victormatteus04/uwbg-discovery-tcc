from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd


def find_final_root(start: Path | None = None) -> Path:
    """Locate the repository's final/ directory from a notebook cwd."""
    start = (start or Path.cwd()).resolve()
    candidates = [start, *start.parents]
    for candidate in candidates:
        if candidate.name == "final":
            return candidate
        child = candidate / "final"
        if child.is_dir():
            return child.resolve()
    raise RuntimeError(f"Could not locate final/ from {start}")


FINAL_ROOT = find_final_root()
REPO_ROOT = FINAL_ROOT.parent
DATA_DIR = FINAL_ROOT / "data"
RUNS_DIR = FINAL_ROOT / "runs"


def ensure_run_dir(run_id: str, run_name: str) -> Path:
    run_dir = RUNS_DIR / f"{run_id}_{run_name}"
    for subdir in ("figures", "outputs"):
        (run_dir / subdir).mkdir(parents=True, exist_ok=True)
    return run_dir


def required_path(path: Path, label: str) -> Path:
    path = path.resolve()
    if not path.exists():
        raise FileNotFoundError(f"{label} not found: {path}")
    return path


def reduced_formula(formula: str) -> str:
    """Return a canonical reduced formula using pymatgen."""
    from pymatgen.core import Composition

    return Composition(str(formula)).reduced_formula


def normalize_layergroup(layergroup: Any) -> str | None:
    if layergroup is None or pd.isna(layergroup):
        return None
    value = str(layergroup).strip().lower().replace(" ", "")
    return value or None


def build_c2db_material_index(c2db_path: Path) -> pd.DataFrame:
    """Build a compact C2DB index for novelty checks."""
    import ase.db

    rows: list[dict[str, Any]] = []
    db = ase.db.connect(str(c2db_path))
    for row in db.select():
        uid = row.key_value_pairs.get("uid")
        formula = row.formula
        try:
            formula_red = reduced_formula(formula)
        except Exception:
            formula_red = str(formula)
        rows.append(
            {
                "uid": uid,
                "formula": formula,
                "reduced_formula": formula_red,
                "natoms": getattr(row, "natoms", None),
                "ehull": getattr(row, "ehull", None),
                "hform": getattr(row, "hform", None),
                "gap_pbe": getattr(row, "gap", None),
                "gap_hse": getattr(row, "gap_hse", None),
                "dyn_stab": getattr(row, "dyn_stab", None),
                "layergroup": getattr(row, "layergroup", None),
                "lgnum": getattr(row, "lgnum", None),
                "international": getattr(row, "international", None),
                "bravais_type": getattr(row, "bravais_type", None),
            }
        )
    df = pd.DataFrame(rows)
    df["layergroup_norm"] = df["layergroup"].map(normalize_layergroup)
    return df


def classify_c2db_novelty(
    formula: str,
    prototype_layergroup: Any,
    c2db_index: pd.DataFrame,
) -> dict[str, Any]:
    """Classify candidate novelty by reduced formula and prototype layergroup."""
    formula_red = reduced_formula(formula)
    layer_norm = normalize_layergroup(prototype_layergroup)

    same_formula = c2db_index[c2db_index["reduced_formula"] == formula_red].copy()
    same_layer = same_formula[same_formula["layergroup_norm"] == layer_norm].copy()

    if same_layer.empty and not same_formula.empty and layer_norm is None:
        novelty_class = "known_composition_unknown_layergroup"
    elif not same_layer.empty:
        novelty_class = "known_material"
    elif not same_formula.empty:
        novelty_class = "known_composition_new_layergroup"
    else:
        novelty_class = "new_composition"

    def pack_values(df: pd.DataFrame, col: str, limit: int = 12) -> str:
        if df.empty or col not in df:
            return ""
        vals = [str(v) for v in df[col].dropna().astype(str).unique()[:limit]]
        return ";".join(vals)

    return {
        "reduced_formula": formula_red,
        "candidate_layergroup": prototype_layergroup,
        "candidate_layergroup_norm": layer_norm,
        "exists_same_formula": bool(not same_formula.empty),
        "exists_same_formula_layergroup": bool(not same_layer.empty),
        "novelty_class": novelty_class,
        "matched_c2db_uids": pack_values(same_formula, "uid"),
        "matched_c2db_layergroups": pack_values(same_formula, "layergroup"),
        "matched_same_lg_uids": pack_values(same_layer, "uid"),
        "matched_same_lg_gap_hse": pack_values(same_layer, "gap_hse"),
        "matched_same_lg_gap_pbe": pack_values(same_layer, "gap_pbe"),
        "matched_same_lg_ehull": pack_values(same_layer, "ehull"),
        "matched_same_lg_dyn_stab": pack_values(same_layer, "dyn_stab"),
    }
