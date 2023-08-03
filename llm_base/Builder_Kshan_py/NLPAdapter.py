import NLPProvider, UserNLPClient

class NLPAdapter:
    @staticmethod
    def getNLPClient(persona: str) -> UserNLPClient.UserNLPClient:
        nlpClient = UserNLPClient.UserNLPClient()
 
        return nlpClient
