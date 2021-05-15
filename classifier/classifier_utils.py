from classifier.classifier import BinaryClassifier, Classifier

def is_classifier_signal_trigger(classifier: Classifier):
    if not (classifier is BinaryClassifier):
        raise Exception("Excepted binary classifier.")

    classifier.__class__ = BinaryClassifier
    return classifier.trigger