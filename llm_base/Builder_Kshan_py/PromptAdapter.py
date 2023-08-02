import PromptBuilder, SyntheticsGPTPromptBuilder

class PromptAdapter:
    @staticmethod
    def get_prompt_builder() -> PromptBuilder:
        prompt_builder = SyntheticsGPTPromptBuilder()
        return prompt_builder
