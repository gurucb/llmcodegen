from typing import List
from abc import ABC, abstractmethod

class IPromptBuilder(ABC):
    @abstractmethod
    def ShowPrompts(self) -> None:
        pass

    @abstractmethod
    def buildPrompts(self, tableschema: List[str], userPrompt: str) -> List[str]:
        pass
