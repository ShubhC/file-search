from classifier.classifier import BinaryClassifier, Classifier
from abc import ABC, abstractmethod
from index.search_index import SearchIndex
from search_plugins.search_plugin_instances import SearchPluginName
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
                 index: SearchIndex,
                 classifier: Classifier) -> None:
        super().__init__()()
        self._search_model_name = search_model_name
        self._index = index
        self._classifier = classifier
     
    @property   
    def classifier(self) -> Classifier:
        return self._classifier

    @property
    def search_model_name(self) -> SearchPluginName:
        return self._search_model_name
    
    @property
    def index(self) -> SearchIndex:
        return self._index

    def search(self, query: str) -> SearchResult:
        classifier = self.classifier
        index_search_results = []

        if classifier is BinaryClassifier:
            classifier.__class__ = BinaryClassifier
            is_classifier_signal_trigger = classifier.trigger()
            if is_classifier_signal_trigger:
                index_search_results = self.index.search_index(query)

            search_result_items = []
            for index_search_result in index_search_results:
                search_result_item = SearchResultItem(index_search_result, 1.0)
                search_result_items.append(search_result_item)

            return SearchResult(self.search_model_name, search_result_items)

        raise NotImplementedError("Only binary classifier is supported.")

    