import classifier
from classifier.classifier import Classifier, BinaryClassifier
from file import File
from typing import List
from search_plugins.search_results import SearchResult, SearchResultItem

class SearchResultConverter:

    @staticmethod
    def from_index_results(index_results: List[File],
                           search_model_name,
                           default_classifier_score: float = -1.0,
                           default_index_score: float = -1.0, 
                           classifier_scores: List[float] = None,
                           index_scores: List[float] = None):
        if classifier_scores:
            assert(len(index_results) == len(classifier_scores), \
                'index_results and classifier scores should be of same size')

        if index_scores:
            assert(len(index_results) == len(index_scores), \
                'index_results and index scores should be of same size')

        search_result_items = []
        for i, index_result in enumerate(index_results):
            
            if index_scores and i < len(index_scores):
                index_score = index_score[i]
            else:
                index_score = default_index_score
            
            if classifier_scores and i < len(classifier_scores):
                classifier_score = classifier_scores[i]
            else:
                classifier_score = default_classifier_score

            search_result_item = SearchResultItem(index_result, 
                                                  classifier_score,
                                                  index_score)
            search_result_items.append(search_result_item)

        return SearchResult(search_model_name, search_result_items)
