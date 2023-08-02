from typing import List

import PromptBuilder

class SyntheticsGPTPromptBuilder(PromptBuilder.PromptBuilder):
    def buildPrompts(self, tableschema: List[str], userPrompt: str) -> List[str]:
        prompts = []
        print("**************************")

        prompts.append("Given an input, generate a syntactically correct SQL Query for MSSQL. In the query, qualify columns as <TableName>.<ColumnName> format.")
        prompts.append("### SQL Tables with their properties:\n")
        prompts.extend(tableschema)
        prompts.append("\n### " + userPrompt + "\nSELECT ")

        return prompts

    def ShowPrompts(self) -> None:
        raise NotImplementedError()
