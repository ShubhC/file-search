from search_request import SearchRequest
from search_plugins.search_plugin_name import SearchPluginName
from search_plugins.search_plugins import SearchPlugin
from classifier.classifier_instances import ClassifierRepo
from index.index_instances import SearchIndexRepo
from search_plugins.search_results import SearchResult
from search_plugins.search_utils import SearchResultConverter

class RegexSearchPlugin(SearchPlugin):

    def __init__(self,
                 search_index_repo: SearchIndexRepo,
                 classifier_repo: ClassifierRepo) -> None:
        search_model_name = SearchPluginName.RegexSearchPlugin
        indexes = [search_index_repo.regex_index]
        classifiers = [classifier_repo.regex_classifier] 
        super().__init__(search_model_name, indexes, classifiers)

    def _search(self, search_request: SearchRequest) -> SearchResult:
        index = self.indexes[0]

        index_results = index.search(search_request.raw_query)

        search_result = SearchResultConverter.from_index_results(index_results = index_results, 
                                                                 search_model_name = self.search_model_name,
                                                                 default_classifier_score=1.0,
                                                                 default_index_score=1.0)
        return search_result

