from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


##load the model
diabetes_model = pickle.load(open('model/diabetes_model.pkl','rb'))


@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters: model_input):
    input_data = input_parameters.json()
    input_dictionary= json.loads(input_data)

    preg = input_dictionary['Pregnencies']
    glu = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin = input_dictionary['SkinThickness']
    insulin = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']

    input_list = [preg,glu,bp,skin,insulin,bmi,dpf,age]

    prediction = diabetes_model.predic([input_list])

    if prediction[0]==0:
        return "Person is not diabetic"
    else:
        return "Person is diabetic"

