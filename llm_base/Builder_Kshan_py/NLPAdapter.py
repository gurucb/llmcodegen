import NLPProvider, UserNLPClient

class NLPAdapter:
    @staticmethod
    def getNLPClient(persona: str) -> NLPProvider:
        nlpClient = UserNLPClient()
 
        return nlpClient
