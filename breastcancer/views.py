'''
from django.shortcuts import render
from django.http import HttpResponse
from breastcancer.tests import predict, predict_proba # Import your prediction functions
import random
from django.views.decorators.csrf import csrf_protect
import os
from django.conf import settings
import joblib
import numpy as np 
from django.shortcuts import render
from django.http import JsonResponse
import joblib
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
import os
file_path = os.path.join(settings.BASE_DIR, "NoteBook", "data3.csv")
data_frame = pd.read_csv("NoteBook/data3.csv")

def home(request):
    return render(request, 'INDEX.html')

def tools(request):
    # Your prediction logic here
    return render(request, 'TOOL.html')

def result(request):
        result1=""
        texture_mean = float(request.GET.get('texture_mean'))
        smoothness_mean = float(request.GET.get('smoothness_mean'))
        compactness_mean = float(request.GET.get('compactness_mean'))
        concave_points_mean = float(request.GET.get('concave points_mean'))
        symmetry_mean = float(request.GET.get('symmetry_mean'))
        fractal_dimension_mean = float(request.GET.get('fractal_dimension_mean'))
        texture_se = float(request.GET.get('texture_se'))
        area_se = float(request.GET.get('area_se'))
        smoothness_se = float(request.GET.get('smoothness_se'))
        compactness_se = float(request.GET.get('compactness_se'))
        concavity_se = float(request.GET.get('concavity_se'))
        concave_points_se =float( request.GET.get('concave points_se'))
        symmetry_se = float(request.GET.get('symmetry_se'))
        fractal_dimension_se = float(request.GET.get('fractal_dimension_se'))
        texture_worst = float(request.GET.get('texture_worst'))
        area_worst = float(request.GET.get('area_worst'))
        smoothness_worst = float(request.GET.get('smoothness_worst'))
        compactness_worst = float(request.GET.get('compactness_worst'))
        concavity_worst = float(request.GET.get('concavity_worst'))
        concave_points_worst = float( request.GET.get('concave points_worst'))
        symmetry_worst = float(request.GET.get('symmetry_worst'))
        fractal_dimension_worst = float(request.GET.get('fractal_dimension_worst'))

        data_frame = pd.read_csv("NoteBook/data3.csv")  # Use double backslashes
        X = data_frame[['texture_mean', 'smoothness_mean', 'compactness_mean', 'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
                        'texture_se', 'area_se','smoothness_se','compactness_se','concavity_se','concave points_se','symmetry_se',
                        'fractal_dimension_se','texture_worst','area_worst','smoothness_worst','compactness_worst',
                        'concavity_worst','concave points_worst','symmetry_worst','fractal_dimension_worst']].values
        y = data_frame['diagnosis'].values
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.25, random_state=78) 
        svc = SVC(probability=True)
        parameters = {'gamma' : [0.0001, 0.001, 0.01, 0.1],'C' : [0.01, 0.05, 0.5, 0.1, 1, 10, 15, 20]}
        grid_search = GridSearchCV(svc, parameters)
        grid_search.fit(X_train, y_train)
        
        svc = SVC(C = 10, gamma = 0.01, probability=True)
        svc.fit(X_train, y_train)
        #rf_model.fit(X_train,y_train.ravel())
        user_data = [[texture_mean, smoothness_mean, compactness_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, texture_se,
                       area_se,smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se,
                        texture_worst, area_worst, smoothness_worst,  compactness_worst, concavity_worst, concave_points_worst, symmetry_worst,
                          fractal_dimension_worst]]
        predict = svc.predict(user_data)
    
        if predict == 1:
            result1 = "Malignant"
        else:
            result1 = "Benign"

   
        return render(request, 'TOOL.html',{"tool":result1})
        '''