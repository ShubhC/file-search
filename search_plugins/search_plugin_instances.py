from pathlib import Path
from adapter.whoosh_adapter import WhooshAdapter
from search_plugins.multi_word_lookup_search_plugin import MultiWordLookupSearchPlugin
from path_store import PathStore
from index.index_instances import SearchIndexRepo
from classifier.classifier_instances import ClassifierRepo
from search_plugins.search_plugins import SearchPlugin
from search_plugins.lookup_search_plugin import LookupSearchPlugin 
from search_plugins.regex_search_plugin import RegexSearchPlugin
from typing import List

class SearchPluginRepo:

    def __init__(self, classifier_repo, path_store, whoosh_adapter) -> None:
        search_index_repo = SearchIndexRepo(whoosh_adapter)
        self._regex_search_plugin = RegexSearchPlugin(search_index_repo, classifier_repo)
        self._multi_word_search_plugin = MultiWordLookupSearchPlugin(search_index_repo, classifier_repo)
    
    @property
    def regex_search_plugin(self) -> SearchPlugin:
        return self._regex_search_plugin

    @property
    def multi_word_search_plugin(self) -> SearchPlugin:
        return self._multi_word_search_plugin
    
    @property
    def all_search_plugin_instances(self) -> List[SearchPlugin]:
        return [self.regex_search_plugin, self.multi_word_search_plugin]
