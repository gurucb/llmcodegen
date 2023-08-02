import MetadataManager, KQLMetadataManager

class DomainAdapter:
    @staticmethod
    def getMetadataManager() -> MetadataManager.MetadataManager:
        metadataManager = KQLMetadataManager.KQLMetadataManager()
        return metadataManager
