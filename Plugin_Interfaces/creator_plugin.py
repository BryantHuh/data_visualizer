from abc import ABC, abstractmethod
from typing import List, Any, TYPE_CHECKING
if TYPE_CHECKING:
    from Domain_Model.data import Data

class CreatorPlugin(ABC):
    @abstractmethod
    def id(self) -> str:
        pass

    @abstractmethod
    def init(self, context: Any) -> None:
        pass

    @abstractmethod
    def createVisualization(self, data: "Data", outPath: str) -> Any:
        pass

    @abstractmethod
    def shutdown(self) -> None:
        pass