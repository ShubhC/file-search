"""
    Entry point for a search query
"""

from search_plugins import lookup_search_plugin
from search_plugins.search_plugin_instances import SearchPluginRepo


search_query = input()
lookup_search_plugin = SearchPluginRepo.LookupSearchPlugin
search_results = lookup_search_plugin.search(search_query)

for search_result_item in search_results._search_result_items:
    print(search_result_item.item.file_name)