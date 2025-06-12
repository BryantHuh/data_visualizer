# Package: Controller
# File: data_controller.py
from Model.data_model import DataModel
from Model.plugin_registry import PluginRegistry
from tkinter import filedialog
from typing import Optional, Any, TYPE_CHECKING
if TYPE_CHECKING:
    from View.main_window import MainWindow
class DataController:
    def __init__(self, model: DataModel, view: "MainWindow", registry: PluginRegistry):
        self.model: DataModel = model
        self.view: MainWindow = view
        self.registry: PluginRegistry = registry

    def onOpen(self, fmt: str) -> None:
        path = filedialog.askopenfilename(filetypes=[(fmt.upper(), f"*.{fmt}")])
        if path:
            self.model.loadFile(path, fmt)

    def onFormatSelect(self, id: str) -> None:
        # Handler stub: implement format change logic if needed
        pass

    def onPluginToggle(self, pid: str) -> None:
        # Deselektieren, falls bereits aktiv
        if self.model._creator_id == pid:
            self.model.setCreator(None)
            return

        # Neues Plugin auswählen
        self.model.setCreator(pid)
        # Nach setCreator ist garantiert ein str gewählt
        assert self.model._creator_id is not None
        creator: str = self.model._creator_id

        # Dateidialog mit sinnvoller Dateityp‐Auswahl
        out = filedialog.asksaveasfilename(
            defaultextension=f".{creator}",
            filetypes=[(creator.upper(), f"*.{creator}")]
        )
        # asksaveasfilename liefert '' bei Abbruch
        if not out:
            return

        # Visualisierung erstellen
        self.model.getVisualization(out)