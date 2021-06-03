from search_request import SearchRequest
from classifier.classifier import BinaryClassifier
from classifier.classifier_names import ClassifierNames
from search_request import SearchMode

class RegexClassifier(BinaryClassifier):
    
    def __init__(self) -> None:
        classifier_name = ClassifierNames.Regex
        super().__init__(classifier_name)

    def predict(self, search_request: SearchRequest):
        return search_request.mode == SearchMode.Regex