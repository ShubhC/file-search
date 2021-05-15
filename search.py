"""
    Entry point for a search query
"""
#import sys
#sys.path.append('.')

from search_plugins.search_plugin_instances import SearchPluginRepo

lookup_search_plugin = SearchPluginRepo.LookupSearchPlugin

while True:
    search_query = input('Enter Search Query ')
    search_results = lookup_search_plugin.search(search_query)

    for search_result_item in search_results._search_result_items:
        print(search_result_item.item.file_path)
