import joblib

from numpy import ndarray, array
from typing import Dict, List

MODEL_PATH: str = "output/randomforest_model.pkl"


def preprocess_data(petal_measures: Dict[str, float]) -> ndarray:        
    """Extract petal measures as a numpy array (column per feature value)"""
    prediction_data: List[float] = [
        petal_measures.get("sepal_length"), 
        petal_measures.get("sepal_width"), 
        petal_measures.get("petal_length"), 
        petal_measures.get("petal_width")
    ]
    
    prediction_data = array(prediction_data).reshape(1,-1)
    
    return prediction_data


def get_local_model(model_path: str):
    """Get locally stored model"""
    with open(model_path,"rb") as path:
        trained_model = joblib.load(path)

    return trained_model


def get_prediction(petal_measures: Dict[str, float]) -> str:
    """Get a prediction for a set of petal measures using a locally stored model"""
    prediction_data: ndarray = preprocess_data(petal_measures)

    trained_model = get_local_model(MODEL_PATH)

    prediction = trained_model.predict(prediction_data)
    
    return prediction
    
