from typing import Any
from Plugin_Interfaces.format_plugin import FormatPlugin
from Domain_Model.data import Data
from Domain_Model.builder import build_tree
import json

class JsonParser(FormatPlugin):
    def id(self) -> str:
        return "json"

    def init(self, context: Any) -> None:
        pass

    def toInternalFormat(self, file_path: str) -> Any:
        with open(file_path, 'r') as f:
            obj = json.load(f)
        return build_tree(None, obj)

    def shutdown(self) -> None:
        pass