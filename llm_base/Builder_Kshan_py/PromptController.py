from typing import List
import NLPAdapter, DomainAdapter, PromptAdapter

class PromptController:
    def __init__(self):
        self.nlp_client = None
        self.kql_metadata_manager = None
        self.table_schema = []
        self.table_names = []
        self.prompts = []
        self.prompt_builder = None
        self.persona = None

    def set_persona(self, persona: str) -> None:
        self.persona = persona

    def initialize_prompt_controller(self) -> None:
        self.nlp_client = NLPAdapter.get_nlp_client(self.persona)
        self.kql_metadata_manager = DomainAdapter.get_metadata_manager()
        self.prompt_builder = PromptAdapter.get_prompt_builder()

    def build_prompts(self, user_prompt: str) -> List[str]:
        self.table_names = self.nlp_client.get_entities(user_prompt)
        self.table_schema = self.kql_metadata_manager.get_object_metadata(self.table_names)
        self.prompts = self.prompt_builder.build_prompts(self.table_schema, user_prompt)

        return self.prompts
