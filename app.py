from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Crear app
app = FastAPI()

# Cargar modelo al iniciar la app
model = joblib.load("regresion_logistica_titanic.pkl")

# Definir esquema de entrada
class Passenger(BaseModel):
    Pclass: int
    Sex: int
    Age: float
    SibSp: int
    Parch: int
    Fare: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(passenger: Passenger):
    data = [[
        passenger.Pclass,
        passenger.Sex,
        passenger.Age,
        passenger.SibSp,
        passenger.Parch,
        passenger.Fare
    ]]

    prediction = model.predict(data)[0]

    return {"survived": int(prediction)}



