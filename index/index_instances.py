from enum import Enum
from dataclasses import dataclass
from index.lookup_index import LookupIndex as LookupIndexClass
from index.index_name import SearchIndexName

@dataclass
class SearchIndexRepo:
    LookupIndex : SearchIndexName = LookupIndexClass()
