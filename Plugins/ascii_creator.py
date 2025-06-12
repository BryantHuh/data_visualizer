from Plugin_Interfaces.creator_plugin import CreatorPlugin
from Domain_Model.node import Node
from Domain_Model.leaf import Leaf
from typing import Any

class AsciiCreator(CreatorPlugin):
    def __init__(self):
        self.context = None

    def id(self) -> str:
        return "ascii"

    def init(self, context: Any) -> None:
        self.context = context

    def createVisualization(self, data: Any, outPath: str) -> str:
        lines = []
        def _rec(node, prefix=""):
            if isinstance(node, Node):
                header = node.key if node.key is not None else '<root>'
                lines.append(f"{prefix}+ {header}")
                for child in node.children:
                    _rec(child, prefix + "  ")
            elif isinstance(node, Leaf):
                lines.append(f"{prefix}- {node.key}: {node.value}")
        _rec(data)
        result = "\n".join(lines)
        with open(outPath, 'w') as f:
            f.write(result)
        return result

    def shutdown(self) -> None:
        pass
