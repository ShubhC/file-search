import classifier
from search_plugins import search_utils
from search_plugins.search_plugins import SearchPlugin
from search_plugins.search_results import SearchResult, SearchResultItem
from classifier.classifier import Classifier
from search_plugins.search_plugin_name import SearchPluginName
from search_plugins.search_utils import SearchResultConverter
from classifier.classifier_instances import ClassifierRepo
from index.index_instances import SearchIndexRepo
from index.search_index import SearchIndex
from typing import List

class LookupSearchPlugin(SearchPlugin):

    def __init__(self) -> None:
        classifiers = [ClassifierRepo.TriggerAllClassifier]
        indexes = [SearchIndexRepo.LookupIndex]
        search_model_name = SearchPluginName.LookupSeachPlugin
        super().__init__(search_model_name, indexes, classifiers)

    def search(self, query: str) -> SearchResult:
        index = self.indexes[0]

        index_results = index.search(query)
        search_result = SearchResultConverter.from_index_results(index_results = index_results, 
                                                                 search_model_name = self.search_model_name,
                                                                 default_classifier_score=1.0,
                                                                 default_index_score=1.0)
        return search_result