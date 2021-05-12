from enum import Enum
from dataclasses import dataclass
from index.lookup_index import LookupIndex as LookupIndexClass

class SearchIndexName(Enum):
    LookupIndex = 0

@dataclass
class SearchIndexRepo:
    LookupIndex : SearchIndexName = LookupIndexClass()
