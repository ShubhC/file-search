from search_request import SearchRequest
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

    def __init__(self, 
                 search_index_repo: SearchIndexRepo,
                 classifier_repo: ClassifierRepo) -> None:
        classifiers = [classifier_repo.multi_word_wildcard_classifier]
        indexes = [search_index_repo.lookup_index]
        search_model_name = SearchPluginName.LookupSeachPlugin
        super().__init__(search_model_name, indexes, classifiers)
    
    def _search(self, search_request: SearchRequest) -> SearchResult:
        index = self.indexes[0]

        index_results = index.search(search_request.raw_query)
        search_result = SearchResultConverter.from_index_results(index_results = index_results, 
                                                                 search_model_name = self.search_model_name,
                                                                 default_classifier_score=1.0,
                                                                 default_index_score=1.0)
        print(type(search_result))
        return search_result