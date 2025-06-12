from Domain_Model.data import Data
from Domain_Model.builder import build_tree
from Plugin_Interfaces.format_plugin import FormatPlugin
from Plugin_Interfaces.creator_plugin import CreatorPlugin
from Model.plugin_registry import PluginRegistry
from typing import Optional, Any

class DataVisualizer:
    def __init__(self, registry: PluginRegistry):
        self.data: Optional[Data] = None
        self.registry = registry

    def loadFile(self, path: str, formatId: str) -> None:
        plugin = self.registry.formats.get(formatId)
        if plugin:
            self.data = plugin.toInternalFormat(path)

    def visualize(self, creatorId: Optional[str], outPath: str) -> Any:
        if self.data and creatorId is not None:
            creator = self.registry.creators.get(creatorId)
            if creator:
                return self.data.accept(creator, outPath)

    def listPlugins(self) -> list[str]:
        return list(self.registry.creators.keys())

    def activatePlugin(self, id: str) -> None:
        pass

    def deactivatePlugin(self, id: str) -> None:
        pass

def main():
    import os
    from Model.plugin_registry import PluginRegistry
    from Model.data_model import DataModel
    from Controller.data_controller import DataController
    from View.main_window import MainWindow

    # 1) Plugins laden und initialisieren
    registry = PluginRegistry()
    plugin_dir = os.path.join(os.path.dirname(__file__), '..', 'Plugins')
    registry.discoverPlugins(plugin_dir)
    registry.initAll(None)  # CoreContext stub: None oder dein Context-Objekt

    # 2) MVC-Komponenten aufsetzen
    visualizer = DataVisualizer(registry)
    model      = DataModel(visualizer)
    # view kommt erst später, daher None als Platzhalter
    controller = DataController(model, None, registry)
    app        = MainWindow(controller)

    # 3) Observer-Pattern aktivieren
    model.addObserver(app)

    # 4) GUI starten
    app.mainloop()

if __name__ == "__main__":
    main()