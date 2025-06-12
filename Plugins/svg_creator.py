from Plugin_Interfaces.creator_plugin import CreatorPlugin
from Domain_Model.node import Node
from Domain_Model.leaf import Leaf
from typing import Any

class SvgCreator(CreatorPlugin):
    def __init__(self):
        self.context = None

    def id(self) -> str:
        return "svg"

    def init(self, context: Any) -> None:
        self.context = context

    def createVisualization(self, data: Any, outPath: str) -> str:
        lines = ["<svg xmlns='http://www.w3.org/2000/svg'>"]
        y = 20
        def _rec(node, indent=0):
            nonlocal y
            text = node.key if isinstance(node, Node) else f"{node.key}: {node.value}"
            lines.append(f"<text x='{10+indent*10}' y='{y}'>{text}</text>")
            y += 20
            if isinstance(node, Node):
                for child in node.children:
                    _rec(child, indent+1)
        _rec(data)
        lines.append("</svg>")
        svg = "\n".join(lines)
        with open(outPath, 'w') as f:
            f.write(svg)
        return svg

    def shutdown(self) -> None:
        pass
