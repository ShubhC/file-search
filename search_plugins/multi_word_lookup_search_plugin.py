from search_plugins.search_plugins import SearchPlugin
from search_plugins.search_plugin_name import SearchPluginName
import search_plugins
from search_plugins import search_results
from search_plugins.search_results import SearchResult
from search_request import SearchMode, SearchRequest
from classifier.classifier_instances import ClassifierRepo
from index.index_instances import SearchIndexRepo
from search_plugins.lookup_search_plugin import LookupSearchPlugin
from search_plugins import search_utils
from search_plugins.search_utils import SearchResultConverter

class MultiWordLookupSearchPlugin(SearchPlugin):

    def __init__(self,
                 search_index_repo: SearchIndexRepo,
                 classifier_repo: ClassifierRepo) -> None:
        classifiers = [classifier_repo.multi_word_wildcard_classifier]
        indexes = [search_index_repo.multi_word_lookup_index] 
        search_model_name = SearchPluginName.MultiWordLookupSearchPlugin
        super().__init__(search_model_name, indexes, classifiers)

    def _search(self, search_request: SearchRequest) -> SearchResult:
        index = self.indexes[0]

        index_results = index.search(search_request.raw_query)
        search_result = SearchResultConverter.from_index_results(index_results = index_results, 
                                                                 search_model_name = self.search_model_name,
                                                                 default_classifier_score=1.0,
                                                                 default_index_score=1.0)
        return search_result