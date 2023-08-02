import MetadataManager, KQLMetadataManager

class DomainAdapter:
    @staticmethod
    def getMetadataManager() -> MetadataManager:
        metadataManager = KQLMetadataManager()
        return metadataManager
