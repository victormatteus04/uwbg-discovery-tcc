"""Batch relaxation with the vendored MatGL source.

This script is intentionally separate from the notebook process so the
fine-tuned MEGNet gap model can keep using the conda MatGL installation that
was used during training, while this process uses the vendored MatGL source
needed by the Hugging Face M3GNet PES model.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path


def _find_final_root(path: Path) -> Path:
    for candidate in [path, *path.parents]:
        if candidate.name == "final":
            return candidate
        nested = candidate / "final"
        if nested.is_dir():
            return nested
    raise RuntimeError(f"Could not locate final/ from {path}")


SCRIPT_PATH = Path(__file__).resolve()
FINAL_ROOT = _find_final_root(SCRIPT_PATH)
VENDORED_MATGL_SRC = FINAL_ROOT / "vendor" / "matgl_src"
if not (VENDORED_MATGL_SRC / "matgl").is_dir():
    raise RuntimeError(f"Vendored MatGL source not found: {VENDORED_MATGL_SRC}")
sys.path.insert(0, str(VENDORED_MATGL_SRC))

import matgl  # noqa: E402
from matgl.ext.ase import Relaxer  # noqa: E402
from pymatgen.core import Structure  # noqa: E402


def _finite_or_none(value: float | None) -> float | None:
    if value is None:
        return None
    value = float(value)
    return value if math.isfinite(value) else None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--model", required=True, type=Path)
    parser.add_argument("--fmax", default=0.10, type=float)
    parser.add_argument("--steps", default=80, type=int)
    args = parser.parse_args()

    potential = matgl.load_model(str(args.model.resolve()))
    relaxer = Relaxer(potential=potential, relax_cell=False)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.input.open("r", encoding="utf-8") as fin, args.output.open("w", encoding="utf-8") as fout:
        for line in fin:
            if not line.strip():
                continue
            item = json.loads(line)
            candidate_index = item["candidate_index"]
            try:
                struct = Structure.from_dict(item["structure"])
                result = relaxer.relax(struct, fmax=args.fmax, steps=args.steps, verbose=False)
                final_structure = result["final_structure"]
                energies = getattr(result.get("trajectory"), "energies", [])
                energy_pa = _finite_or_none(energies[-1] / len(final_structure) if energies else None)
                payload = {
                    "candidate_index": candidate_index,
                    "relaxation_status": "relaxed",
                    "relaxation_message": "",
                    "m3gnet_energy_pa_relaxed": energy_pa,
                    "final_structure": final_structure.as_dict(),
                }
            except Exception as exc:  # keep batch resilient
                payload = {
                    "candidate_index": candidate_index,
                    "relaxation_status": "relax_failed",
                    "relaxation_message": f"{type(exc).__name__}: {exc}",
                    "m3gnet_energy_pa_relaxed": None,
                    "final_structure": None,
                }
            fout.write(json.dumps(payload) + "\n")
            fout.flush()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
