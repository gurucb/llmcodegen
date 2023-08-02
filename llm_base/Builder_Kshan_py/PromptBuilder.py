from typing import List
from abc import ABC, abstractmethod

import IPromptBuilder

class PromptBuilder(IPromptBuilder.IPromptBuilder):
    @abstractmethod
    def buildPrompts(self, tableschema: List[str], userPrompt: str) -> List[str]:
        pass

    @abstractmethod
    def ShowPrompts(self) -> None:
        pass
