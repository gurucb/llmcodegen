from typing import List
from abc import ABC, abstractmethod

class IMetadataManager(ABC):
    @abstractmethod
    def getObjectMetadata(self, objectName: List[str]) -> List[str]:
        pass
