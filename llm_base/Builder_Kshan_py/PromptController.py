from typing import List
import NLPAdapter, DomainAdapter, PromptAdapter, UserNLPClient, KQLMetadataManager, SyntheticsGPTPromptBuilder

class PromptController:
    def __init__(self):
        self.nlp_client = None
        self.kql_metadata_manager = None
        self.table_schema = []
        self.table_names = []
        self.prompts = []
        self.persona = None

    def set_persona(self, persona: str) -> None:
        self.persona = persona

    def initialize_prompt_controller(self) -> None:
        self.nlp_client = NLPAdapter.NLPAdapter.getNLPClient(self.persona)
        self.kql_metadata_manager = DomainAdapter.DomainAdapter.getMetadataManager()
        self.prompt_builder = PromptAdapter.PromptAdapter.get_prompt_builder()

    def build_prompts(self, user_prompt: str) -> List[str]:
        self.table_names = self.nlp_client.getEntities(user_prompt)
        self.table_schema = self.kql_metadata_manager.getObjectMetadata(self.table_names)
        self.prompts = SyntheticsGPTPromptBuilder.SyntheticsGPTPromptBuilder.buildPrompts(self, self.table_schema, user_prompt)

        return self.prompts
