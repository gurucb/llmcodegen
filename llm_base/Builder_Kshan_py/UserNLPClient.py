from typing import List

import NLPProvider

class UserNLPClient(NLPProvider):
    def __init__(self):
        pass

    def getEntities(self, userPrompt: str) -> List[str]:
        tableNames = []
        words = userPrompt.split(' ')

        if "Sybase_Results" in words:
            tableNames.append("Sybase_Results")

        if "CassandraTestSummary" in words:
            tableNames.extend(["CassandraTestSummary", "DeploymentMetadata", "TestInfraMetadata"])

        if "SockPerf_Results" in words:
            tableNames.extend(["SockPerf_Results", "DeploymentMetadata", "TestInfraMetadata"])

        if "TestRunDetails" in words:
            tableNames.extend(["TestRunDetails", "DeploymentMetadata", "TestInfraMetadata"])

        if "DeploymentMetadata" in words:
            tableNames.append("DeploymentMetadata")

        if "TestInfraMetadata" in words:
            tableNames.append("TestInfraMetadata")

        return tableNames

    def getIntents(self, userPrompt: str) -> List[str]:
        raise NotImplementedError()
