from typing import List
from abc import ABC, abstractmethod

import IMetadataManager

class MetadataManager(IMetadataManager.IMetadataManager):
    @abstractmethod
    def getObjectMetadata(self, objectName: List[str]) -> List[str]:
        pass
