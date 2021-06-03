from search_request import SearchRequest
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

    def is_domain_query(self, search_request: SearchRequest) -> SearchResult:
        for classifier in self.classifiers:
            if not classifier.predict(search_request):
                return False
        return True

    @abstractmethod
    def _search(self, search_request: SearchRequest) -> SearchResult:
        pass 

    def search(self, search_request: SearchRequest) -> SearchResult:
        if not self.is_domain_query(search_request):
            return None
        return self._search