from Domain_Model.data import Data
from typing import List, Any
from Plugin_Interfaces.creator_plugin import CreatorPlugin


class Leaf(Data):
    def __init__(self, key: str, value: Any):
        super().__init__(key)
        self.value = value

    def accept(self, plugin: 'CreatorPlugin', outPath: str) -> Any:
        return plugin.createVisualization(self, outPath)