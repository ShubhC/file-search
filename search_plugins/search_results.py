from search_plugins.search_plugin_name import SearchPluginName
from typing import List
from file import File

class SearchResultItem:    
    def __init__(self, 
                 item: File,
                 classifier_score: float,
                 index_score: float) -> None:
        self._item = item
        self._classifier_score = classifier_score
        self._index_score = index_score
    
    @property
    def item(self) -> File:
        return self._item
    
    @property
    def classifier_score(self) -> float:
        return self._classifier_score

    @property
    def index_score(self) -> float:
        return self._index_score

class SearchResult:

    def __init__(self,
                 search_plugin_name: SearchPluginName, 
                 search_result_items: List[SearchResultItem]) -> None:
        self._search_plugin_name = search_plugin_name
        self._search_result_items = search_result_items
        
    @property
    def search_plugin_name(self) -> SearchPluginName:
        return self._search_plugin_name
    
    @property
    def search_results(self) -> List[SearchResultItem]:
        return self._search_result_items