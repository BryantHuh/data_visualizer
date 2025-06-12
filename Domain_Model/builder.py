from typing import Any, Optional
from Domain_Model.data import Data
from Domain_Model.node import Node
from Domain_Model.leaf import Leaf


def build_tree(key: Optional[str], obj: Any) -> Data:
    actual_key = key if key is not None else 'root'
    if isinstance(obj, dict):
        node = Node(actual_key)
        for k, v in obj.items():
            node.children.append(build_tree(k, v))
        return node
    elif isinstance(obj, list):
        node = Node(actual_key)
        for idx, item in enumerate(obj):
            node.children.append(build_tree(str(idx), item))
        return node
    else:
        return Leaf(actual_key, obj)
