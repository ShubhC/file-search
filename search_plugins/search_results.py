from search_plugins.search_plugins import SearchModelName
from typing import List
from file_store import File

class SearchResultItem:    
    def __init__(self, item: File, score) -> None:
        self._item = item
        self._score = score
    
    @property
    def item(self) -> File:
        return self._item
    
    @property
    def score(self) -> float:
        return self._score

class SearchResult:

    def __init__(self, model_name: SearchModelName, search_result_items: List[SearchResultItem]) -> None:
        self._model_name = model_name
        self._search_result_items = search_result_items
        
    @property
    def model_name(self) -> SearchModelName:
        return self._model_name
    
    @property
    def search_results(self):
        return self._search_result_items