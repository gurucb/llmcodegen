import LLMClient, GPTClient

class LLMApater:
    @staticmethod
    def get_llm_instance() -> LLMClient:
        llm_client = GPTClient()
        return llm_client
