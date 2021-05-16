from classifier.classifier import Classifier
from classifier.trigger_all_classifier import TriggerAllClassifier
        
class ClassifierRepo:

    def __init__(self) -> None:
        self._trigger_all_classifier = TriggerAllClassifier()

    @property
    def trigger_all_classifier(self) -> Classifier:
        return self._trigger_all_classifier