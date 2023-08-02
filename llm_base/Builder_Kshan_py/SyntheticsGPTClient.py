import NLPAdapter, DomainAdapter, LLMAdapter, PromptController

class SyntheticsGPTClient:
    def __init__(self):
        self.nlp_client = None
        self.kql_metadata_manager = None
        self.gpt_client = None
        self.prompts = []
        self.model = ""

    async def get_kql_output(self):
        prompt_controller = PromptController.PromptController()
        self.prompts = prompt_controller.build_prompts("From tables TestRunDetails and Resources generate KQL Query to retrieve only last 10 resource names that ran 'Sybase' tests based on datetime")
        
        self.gpt_client = LLMAdapter.LLMAdapter.get_llm_instance()
        self.gpt_client.set_properties()
        await self.gpt_client.invoke_llm_command_async(self.prompts, self.model)


