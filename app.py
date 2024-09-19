import pickle
from flask import Flask, request, jsonify
from index.index_instances import SearchIndexRepo
from search_plugins.search_results import SearchResult
from classifier.classifier_instances import ClassifierRepo
from path_store import PathStore
from adapter.whoosh_adapter import WhooshAdapter
from search_request import SearchMode, SearchRequest
from search_plugins import regex_search_plugin
from search_plugins.search_plugin_instances import SearchPluginRepo
import os
from quickstart import generate_keywords
from pathlib import Path
import time
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

def get_name_from_path(path):
    return os.path.basename(path)

def print_search_results(search_result: SearchResult) -> list:
    results = []
    if not search_result:
        return results
    for search_item in search_result.search_results:
        file_path = Path(search_item.item)
        # Get file name
        file_name = file_path.name
        # Get file size in bytes
        file_size = file_path.stat().st_size
        
        # Get creation time
        created_at = time.ctime(os.path.getctime(file_path))
        # Get modification time
        modified_at = time.ctime(os.path.getmtime(file_path))

        results.append({
            'classifier_score': search_item.classifier_score,
            'index_score': search_item.index_score,
            'file': str(search_item.item),
            'file_name': file_name,
            'created_at': created_at,
            'modifies_at': modified_at,
            'file_size': file_size
        })
    return results

def rank_files(query, files):
    def rank_key(file):
        file_name = file['file_name'].lower()
        lower_query = query.lower()
        position = file_name.find(lower_query)
        count = file_name.count(lower_query)
        return (position, -count, file_name)

    ranked_files = sorted(files, key=rank_key)
    return ranked_files

def highlight_query_in_files(query, files):
    def find_query_positions(file_name, query):
        positions = []
        start = file_name.find(query)
        while start != -1:
            end = start + len(query) - 1
            positions.append([start, end])
            start = file_name.find(query, start + 1)
        return positions

    for file in files:
        file_name = file['file_name'].lower()
        lower_query = query.lower()
        words = lower_query.split()
        file['highlighter'] = []
        for word in words:
            file['highlighter'].extend(find_query_positions(file_name, word))
    
    return files

indexing_done_flag = False
pickle_file = 'search_plugin_repo.pkl'
if os.path.exists(pickle_file):
    indexing_done_flag = True

# init vars
classifier_repo = ClassifierRepo(indexing_done_flag)
path_store = PathStore(indexing_done_flag)
whoosh_adapter = WhooshAdapter(path_store, indexing_done_flag)

# Check if the pickle file exists
if indexing_done_flag:
    with open(pickle_file, 'rb') as f:
        search_plugin_repo = pickle.load(f)
else:
    search_plugin_repo = SearchPluginRepo(classifier_repo, path_store, whoosh_adapter)
    with open(pickle_file, 'wb') as f:
        pickle.dump(search_plugin_repo, f)

# all search plugin instances
all_search_plugin_instances = search_plugin_repo.all_search_plugin_instances

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    search_query = data.get('query')
    
    search_request = SearchRequest(search_query, SearchMode.Empty)
    results = []

    for search_plugin in all_search_plugin_instances:
        search_result = search_plugin.search(search_request)
        results.extend(print_search_results(search_result))

    ranked_files = rank_files(search_query, results)
    highlighted_files = highlight_query_in_files(search_query, ranked_files)

    return jsonify(highlighted_files)

@app.route('/deep-search', methods=['POST'])
def deep_search():
    data = request.get_json()
    search_query = data.get('query')
     # Generate keywords using quickstart.py
    keywords = generate_keywords(search_query)

    # Split the keywords into a list
    keyword_list = [keyword.strip() for keyword in keywords.split(',')]

    search_request = SearchRequest(search_query, SearchMode.Empty)
    results = []

    # call each search plugin to get results
    for keyword in keyword_list:
        print(keyword)
        search_request = SearchRequest(keyword, SearchMode.Empty)
        for search_plugin in all_search_plugin_instances:
            search_result = search_plugin.search(search_request)
            results.extend(print_search_results(search_result))
        results = rank_files(keyword, results)
        results = highlight_query_in_files(keyword, results)
    

    return jsonify(results)

if __name__ == '__main__':
    subprocess.Popen(['python', 'C:\\Users\\dechauhan\\file-search\\file_event_listener.py'])
    app.run(debug=True)