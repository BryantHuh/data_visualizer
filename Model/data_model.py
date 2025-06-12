from Domain_Model.data import Data
from Model.data_visualizer import DataVisualizer
from typing import Optional, Any, List

class DataModel:
    def __init__(self, visualizer: DataVisualizer):
        self.visualizer: DataVisualizer = visualizer
        self.currentData: Optional[Data] = None
        self._creator_id: Optional[str] = ""
        self._observers: List[Any] = []

    def addObserver(self, obs: Any) -> None:
        self._observers.append(obs)

    def notify(self) -> None:
        for obs in self._observers: obs.update()

    def loadFile(self, path: str, fmt: str) -> None:
        self.visualizer.loadFile(path, fmt)
        self.currentData = self.visualizer.data
        self.notify()

    def setCreator(self, id: Optional[str]) -> None:
        self._creator_id = id
        self.notify()

    def getVisualization(self, outPath: str) -> None:
        if self._creator_id is None:
            raise RuntimeError("Kein Creator-Plugin ausgewählt!")
        # ab hier ist self._creator_id ein str
        self.visualizer.visualize(self._creator_id, outPath)