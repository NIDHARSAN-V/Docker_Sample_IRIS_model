from fastapi import FastAPI
import numpy as np
import joblib

# Load the model from the correct path
model = joblib.load('/iris_model/iris_model.joblib')  # Adjusted the path to match where Dockerfile copies it

class_names = np.array(['setosa', 'versicolor', 'virginica'])  
app = FastAPI()

@app.get("/")
def read_root():
    return {'message': 'Iris model API'}

@app.post("/predict")
def predict(data: dict):
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    class_name = class_names[prediction][0]
    return {'Predicted_class': class_name}
