import PromptController, LLMAdapter, QueryExecutionAdapter
import json

import asyncio

async def test():
    query = input("Enter your query: ")
    table = input("Enter table name: ")

    user_prompt = f"{query} from {table}"

    prompt_controller = PromptController.PromptController()
    prompt_controller.set_persona("user")
    prompt_controller.initialize_prompt_controller()
    prompts = prompt_controller.build_prompts(user_prompt)

    llm_client = LLMAdapter.LLMAdapter.get_llm_instance()
    llm_client.set_properties()
    kql_query = await llm_client.invoke_llm_command_async(prompts, "")

    query = f"Select {kql_query}".replace('/n', ' ')

    print(query)

    executor = QueryExecutionAdapter.QueryExecutionAdapter.get_query_executor()
    json_data = await executor.execute_query("sql", query)

    print(json_data)

    if not json_data:
        json_data = json.dumps({"data": [{"Results": "No records in DB"}]})

    


asyncio.run(test())

