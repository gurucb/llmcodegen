from typing import List
import abc

class ILLMClient(abc.ABC):
    @abc.abstractmethod
    async def invoke_llm_command_async(self, prompts: List[str], model: str) -> str:
        pass
