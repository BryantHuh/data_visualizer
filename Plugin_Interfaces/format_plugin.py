
from abc import ABC, abstractmethod
from Domain_Model.data import Data
from typing import List, Any

class FormatPlugin(ABC):
    @abstractmethod
    def id(self) -> str:
        pass

    @abstractmethod
    def init(self, context: Any) -> None:
        pass

    @abstractmethod
    def toInternalFormat(self, file_path: str) -> Data:
        pass

    @abstractmethod
    def shutdown(self) -> None:
        pass