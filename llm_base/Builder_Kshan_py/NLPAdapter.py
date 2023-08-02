import NLPProvider, UserNLPClient

class NLPAdapter:
    @staticmethod
    def getNLPClient(persona: str) -> NLPProvider.NLPProvider:
        nlpClient = UserNLPClient.UserNLPClient()
 
        return nlpClient
