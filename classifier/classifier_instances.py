from classifier.classifier import Classifier
from classifier.trigger_all_classifier import TriggerAllClassifier
from enum import Enum
from dataclasses import dataclass
    
class ClassifierNames(Enum):
    TriggerAll = 0
    
@dataclass
class ClassifierRepo:
    TriggerAllClassifier : Classifier = TriggerAllClassifier()