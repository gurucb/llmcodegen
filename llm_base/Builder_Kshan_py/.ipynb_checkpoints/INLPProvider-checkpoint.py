from typing import List
from abc import ABC, abstractmethod

class INLPProvider(ABC):
    @abstractmethod
    def getIntents(self, userPrompt: str) -> List[str]:
        pass

    @abstractmethod
    def getEntities(self, userPrompt: str) -> List[str]:
        pass