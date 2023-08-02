from typing import List
from azure.ai.language.lro import CompletionsOptions
from azure.core.credentials import AzureKeyCredential
from azure.ai.language import LanguageModelCredential, LanguageModelApi

import LLMClient

class GPTClient(LLMClient):
    def __init__(self):
        super().__init__()
        self.model_name = "syntheticsKQL"

    async def get_completions_async(self, prompts: List[str]) -> str:
        final_prompt = "\n".join(prompts)

        completions_options = CompletionsOptions(
            prompts=[final_prompt],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            stop_sequences=["#", ";"],
            nucleus_sampling_factor=self.nucleus_sampling_factor,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty
        )

        completions_response = await self.oai_client.begin_completions(
            deployment_or_model_name=self.model_name,
            options=completions_options
        ).result()

        completions = completions_response.value
        response_kql = completions[0].text
        return response_kql

    async def invoke_llm_command_async(self, prompts: List[str], model: str) -> str:
        kql_query = await self.get_completions_async(prompts)
        return kql_query
