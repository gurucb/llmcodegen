import LLMClient, GPTClient

class LLMAdapter:
    @staticmethod
    def get_llm_instance() -> LLMClient.LLMClient:
        llm_client = GPTClient.GPTClient()
        return llm_client
