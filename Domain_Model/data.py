from abc import ABC, abstractmethod
from typing import List, Any, TYPE_CHECKING
if TYPE_CHECKING:
    from Plugin_Interfaces.format_plugin import FormatPlugin
    from Plugin_Interfaces.creator_plugin import CreatorPlugin


class Data(ABC):
    def __init__(self, key: str):
        self.key = key

    @abstractmethod
    def accept(self, plugin: 'CreatorPlugin', outPath: str) -> Any:
        pass