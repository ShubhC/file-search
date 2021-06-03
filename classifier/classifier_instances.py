from classifier.regex_classifier import RegexClassifier
from classifier.multi_word_wildcard_classifier import MultiWordWildcardClassifier
from classifier.classifier import Classifier
from classifier.trigger_all_classifier import TriggerAllClassifier
        
class ClassifierRepo:

    def __init__(self) -> None:
        self._trigger_all_classifier = TriggerAllClassifier()
        self._multi_word_wildcard_classifier = MultiWordWildcardClassifier()
        self._regex_classifier = RegexClassifier()

    @property
    def trigger_all_classifier(self) -> Classifier:
        return self._trigger_all_classifier
    
    @property
    def multi_word_wildcard_classifier(self) -> Classifier:
        return self._multi_word_wildcard_classifier
    
    @property
    def regex_classifier(self) -> Classifier:
        return self._regex_classifier