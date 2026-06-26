function parseReplication(value) {
  if (!value) return [1, 1, 1];
  const parts = value.split(",").map((part) => Number.parseInt(part.trim(), 10));
  if (parts.length !== 3 || parts.some((part) => Number.isNaN(part) || part < 1)) {
    return [1, 1, 1];
  }
  return parts;
}

function showViewerMessage(container, message) {
  container.innerHTML = "";
  const paragraph = document.createElement("p");
  paragraph.className = "viewer3d__message";
  paragraph.textContent = message;
  container.appendChild(paragraph);
}

async function loadStructureViewer(container) {
  if (!window.$3Dmol) {
    showViewerMessage(container, "Visualizador 3D indisponível. Recarregue a página com acesso à internet.");
    return;
  }

  const structurePath = container.dataset.structure;
  const label = container.dataset.label || "estrutura";

  try {
    const response = await fetch(structurePath);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const cif = await response.text();
    container.innerHTML = "";

    const viewer = window.$3Dmol.createViewer(container, {
      backgroundColor: "white",
      antialias: true,
    });

    viewer.addModel(cif, "cif");

    const [nx, ny, nz] = parseReplication(container.dataset.replicate);
    if (nx > 1 || ny > 1 || nz > 1) {
      try {
        viewer.replicateUnitCell(nx, ny, nz);
      } catch {
        // A visualização continua funcional mesmo quando a replicação da célula não está disponível.
      }
    }

    viewer.setStyle({}, {
      stick: { radius: 0.13, colorscheme: "Jmol" },
      sphere: { scale: 0.32, colorscheme: "Jmol" },
    });
    viewer.addUnitCell({ color: "#64748b" });
    viewer.zoomTo();
    viewer.render();
  } catch (error) {
    showViewerMessage(container, `Não foi possível carregar ${label} em 3D.`);
    console.error(`Erro ao carregar ${structurePath}:`, error);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".viewer3d").forEach((container) => {
    loadStructureViewer(container);
  });
});
