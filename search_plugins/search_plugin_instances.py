from enum import Enum
from dataclasses import dataclass
from search_plugins.search_plugins import SearchPlugin
from search_plugins.lookup_search_plugin import LookupSearchPlugin as LookupSearchPluginClass
    
@dataclass
class SearchPluginRepo:
    LookupSearchPlugin : SearchPlugin = LookupSearchPluginClass()
