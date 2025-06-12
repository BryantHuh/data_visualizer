from Plugin_Interfaces.format_plugin import FormatPlugin
from Plugin_Interfaces.creator_plugin import CreatorPlugin
from Plugins.json_parser import JsonParser
from Plugins.yaml_parser import YamlParser
from Plugins.ascii_creator import AsciiCreator
from Plugins.svg_creator import SvgCreator
from Domain_Model.data import Data
from typing import Any

class PluginRegistry:
    def __init__(self):
        self.formats: dict[str, FormatPlugin] = {}
        self.creators: dict[str, CreatorPlugin] = {}

    def discoverPlugins(self, dir: str) -> None:
        self.formats = {p.id(): p for p in [JsonParser(), YamlParser()]}
        self.creators = {p.id(): p for p in [AsciiCreator(), SvgCreator()]}

    def initAll(self, ctx: Any) -> None:
        for p in (*self.formats.values(), *self.creators.values()): p.init(ctx)

    def shutdownAll(self) -> None:
        for p in (*self.formats.values(), *self.creators.values()): p.shutdown()

    def getMetadata(self) -> list[str]:
        return list(self.creators.keys())