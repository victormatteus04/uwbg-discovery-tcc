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
  const format = container.dataset.format || structurePath.split(".").pop();
  const label = container.dataset.label || "estrutura";

  try {
    const response = await fetch(structurePath);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const structure = await response.text();
    container.innerHTML = "";

    const viewer = window.$3Dmol.createViewer(container, {
      backgroundColor: "white",
      antialias: true,
    });

    viewer.addModel(structure, format, { assignBonds: true });
    viewer.setStyle({}, {
      stick: { radius: 0.14, colorscheme: "Jmol" },
      sphere: { scale: 0.24, colorscheme: "Jmol" },
    });
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
