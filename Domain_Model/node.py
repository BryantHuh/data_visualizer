from Plugin_Interfaces.creator_plugin import CreatorPlugin
from typing import List, Optional, Any
from Domain_Model.data import Data

class Node(Data):
    def __init__(self, key: str):
        super().__init__(key)
        self.children: List[Data] = []

    def accept(self, plugin: 'CreatorPlugin', outPath: str) -> Any:
        return plugin.createVisualization(self, outPath)