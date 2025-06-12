import yaml
from Domain_Model.builder import build_tree
from Plugin_Interfaces.format_plugin import FormatPlugin
from typing import Any

class YamlParser(FormatPlugin):
    def id(self) -> str:
        return "yaml"

    def init(self, context: Any) -> None:
        pass

    def toInternalFormat(self, file_path: str) -> Any:
        with open(file_path, 'r') as f:
            obj = yaml.safe_load(f)
        return build_tree(None, obj)

    def shutdown(self) -> None:
        pass
