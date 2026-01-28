# Titanic API – Cloud Computing Project

Este proyecto implementa un modelo de Machine Learning entrenado con el dataset de Titanic y lo expone mediante una API REST utilizando FastAPI, desplegada en Google Cloud Run, sin docker,

Accuracy en test: 0.810

## Descripción
El objetivo es demostrar el ciclo completo de un modelo de datos:
- Entrenamiento de modelo en Python
- Exposición mediante una API REST
- Despliegue en la nube (Cloud Run)

El modelo predice si un pasajero sobrevive o no al hundimiento del Titanic.

## Tecnologías utilizadas
- Python 3.10
- Scikit-learn
- FastAPI
- Uvicorn
- Google Cloud Run
- Google Cloud Build
- GitHub

## Endpoints disponibles

### Health check
```
GET /health
```

### Predicción
```
POST /predict
```

Ejemplo de request:
```json
{
  "Pclass": 0,
  "Sex": 1,
  "Age": 10,
  "SibSp": 0,
  "Parch": 0,
  "Fare": 0
}
```

Ejemplo de response:
```json
{
  "survived": 1
}
```

## Documentación Swagger
La documentación interactiva de la API está disponible en:
```
/docs
```

URL pública:
https://titanic-api-880026336002.europe-west1.run.app/docs

URL health:
https://titanic-api-880026336002.europe-west1.run.app/health

## Despliegue
El servicio está desplegado en Google Cloud Run y se construye automáticamente desde GitHub utilizando Cloud Build.

URL del servicio:
https://titanic-api-880026336002.europe-west1.run.app

## Repositorio
https://github.com/alejandraveliz-crypto/titanic_api

## Equipo
Ale
Leo
JP
