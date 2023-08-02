import PromptBuilder, SyntheticsGPTPromptBuilder

class PromptAdapter:
    @staticmethod
    def get_prompt_builder() -> PromptBuilder.PromptBuilder:
        prompt_builder = SyntheticsGPTPromptBuilder.SyntheticsGPTPromptBuilder()
        return prompt_builder
