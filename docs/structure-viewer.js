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
  const fallbackStructurePath = container.dataset.fallbackStructure;
  const fallbackFormat = container.dataset.fallbackFormat || fallbackStructurePath?.split(".").pop();
  const label = container.dataset.label || "estrutura";

  async function fetchStructure(path) {
    const response = await fetch(path);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    return response.text();
  }

  function renderStructure(structure, structureFormat) {
    container.innerHTML = "";
    const viewer = window.$3Dmol.createViewer(container, {
      backgroundColor: "white",
      antialias: true,
    });

    viewer.addModel(structure, structureFormat, { assignBonds: true });
    viewer.setStyle({}, {
      stick: { radius: 0.14, colorscheme: "Jmol" },
      sphere: { scale: 0.24, colorscheme: "Jmol" },
    });
    viewer.zoomTo();
    viewer.render();
  }

  try {
    renderStructure(await fetchStructure(structurePath), format);
  } catch (error) {
    console.warn(`Erro ao carregar ${structurePath}; tentando fallback.`, error);

    if (fallbackStructurePath) {
      try {
        renderStructure(await fetchStructure(fallbackStructurePath), fallbackFormat);
        return;
      } catch (fallbackError) {
        console.error(`Erro ao carregar fallback ${fallbackStructurePath}:`, fallbackError);
      }
    }

    showViewerMessage(container, `Não foi possível carregar ${label} em 3D.`);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".viewer3d").forEach((container) => {
    loadStructureViewer(container);
  });
});
