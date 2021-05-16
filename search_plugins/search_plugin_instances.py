from file_store import FileStore
from index.index_instances import SearchIndexRepo
from classifier.classifier_instances import ClassifierRepo
from search_plugins.search_plugins import SearchPlugin
from search_plugins.lookup_search_plugin import LookupSearchPlugin 
from search_plugins.regex_search_plugin import RegexSearchPlugin

class SearchPluginRepo:

    def __init__(self) -> None:
        file_store = FileStore()
        classifier_repo = ClassifierRepo()
        search_index_repo = SearchIndexRepo(file_store)
        self._lookup_search_plugin = LookupSearchPlugin(search_index_repo, classifier_repo)
        self._regex_search_plugin = RegexSearchPlugin(search_index_repo, classifier_repo)

    @property
    def lookup_search_plugin(self) -> SearchPlugin:
        return self._lookup_search_plugin
    
    @property
    def regex_search_plugin(self) -> SearchPlugin:
        return self._regex_search_plugin

