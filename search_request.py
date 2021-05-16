from enum import Enum

class SearchMode(Enum):
    Empty = 0
    Regex = 1

class SearchRequest:

    def __init__(self,
                 raw_query: str,
                 mode: SearchMode) -> None:
        self._raw_query = raw_query
        self._mode = mode

    @property
    def raw_query(self):
        return self._raw_query
    
    @property
    def mode(self):
        return self._mode
