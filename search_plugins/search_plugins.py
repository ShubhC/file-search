from classifier.classifier import BinaryClassifier, Classifier
from abc import ABC, abstractmethod
from index.search_index import SearchIndex
from search_plugins.search_plugin_name import SearchPluginName
from search_plugins.search_results import SearchResult, SearchResultItem
from typing import List

class SearchPlugin(ABC):
    """
        Abstract class for search plugins
        All search plugins are stateless and 
        only act on the current user query.
    """
    
    @abstractmethod
    def __init__(self,
                 search_model_name: SearchPluginName, 
                 indexes: List[SearchIndex],
                 classifiers: List[Classifier]) -> None:
        self._search_model_name = search_model_name
        self._indexes = indexes
        self._classifiers = classifiers
     
    @property   
    def classifiers(self) -> List[Classifier]:
        return self._classifiers

    @property
    def search_model_name(self) -> SearchPluginName:
        return self._search_model_name
    
    @property
    def indexes(self) -> List[SearchIndex]:
        return self._indexes

    @abstractmethod
    def search(self, query: str) -> SearchResult:
        pass