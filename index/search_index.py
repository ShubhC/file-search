from abc import ABC, abstractmethod
from enum import Enum
from file import File
from index.index_name import SearchIndexName
from typing import List

class SearchIndex(ABC):
    
    def __init__(self, index_name : SearchIndexName) -> None:
        self._index_name = index_name
        
    @property
    def index_name(self):
        return self._index_name
    
    @abstractmethod
    def search(self, query: str, **kwargs) -> List[File]:
        pass