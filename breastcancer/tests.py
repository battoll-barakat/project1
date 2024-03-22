from django.test import TestCase
import pickle

# Create your tests here.
import joblib 
def predict(data):
    model = joblib.load('ml_model/breast_cancer.pkl')
    return model.predict(data)

def predict_proba(data):
    model = joblib.load('ml_model/breast_cancer.pkl')
    return model.predict_proba(data)

