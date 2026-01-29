# Titanic API – Cloud Computing Project

Este proyecto utiliza el dataset clásico de Titanic para demostrar el ciclo completo de operacionalización de un modelo de Machine Learning en la nube: desde el entrenamiento hasta su exposición como API REST y despliegue en producción en Google Cloud Run, sin Docker.

El modelo resuelve un problema de **clasificación binaria**, prediciendo si un pasajero sobrevive (`1`) o no (`0`) al hundimiento del Titanic.


---

## Descripción del problema

El objetivo es mostrar el flujo end-to-end de un modelo de datos en un entorno cloud real:

- Entrenamiento de un modelo de clasificación en Python  
- Exportación del modelo entrenado a un archivo `.pkl`  
- Exposición del modelo mediante una API REST con FastAPI  
- Despliegue de la API en la nube usando Google Cloud Run  
- Consumo del modelo a través de una URL pública  

---

## Modelo de Machine Learning

- **Tipo de problema:** Clasificación binaria (supervivencia de pasajeros)  
- **Dataset:** Titanic  
- **Target:** `Survived`  
- **Features utilizadas en la API:**  
  - `Pclass`  
  - `Sex` (codificado como 0/1)  
  - `Age`  
  - `SibSp`  
  - `Parch`  
  - `Fare`  
- **Modelo:** Regresión Logística (scikit-learn)  
- **Métrica principal:** Accuracy en conjunto de test: 0.810  

Si bien la métrica principal reportada es accuracy, el dataset presenta cierto desbalance entre clases, por lo que métricas como **precision**, **recall** y **F1-score** también resultan relevantes para una evaluación más completa del desempeño del modelo. No obstante, para efectos de esta tarea se prioriza accuracy, dado que el foco está en la operacionalización y despliegue del modelo en cloud.

El modelo entrenado se guarda como archivo `.pkl` y se carga al iniciar la aplicación FastAPI (no se reentrena dentro de la API).

---

## Cómo ejecutar la API localmente

### 1. Clonar el repositorio

```bash
git clone https://github.com/alejandraveliz-crypto/titanic_api.git
cd titanic_api
```

### 2. Crear entorno virtual (opcional pero recomendado)

```bash
python -m venv titanic
# Linux / macOS
source titanic/bin/activate
# Windows (PowerShell)
titanic\Scripts\Activate.ps1
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Levantar la API con Uvicorn

```bash
uvicorn app:app --reload
```

La API quedará disponible en:

- Swagger UI: http://127.0.0.1:8000/docs  
- Health check: http://127.0.0.1:8000/health  
- Endpoint de predicción: http://127.0.0.1:8000/predict  

---

## Endpoints disponibles

### Health check

```http
GET /health
```

---

### Predicción

```http
POST /predict
```

#### Ejemplo de request

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

#### Ejemplo de response

```json
{
  "survived": 1
}
```

---

## Documentación interactiva (Swagger)

Disponible en:

```
/docs
```

### URL pública de Swagger
https://titanic-api-880026336002.europe-west1.run.app/docs

### URL health pública
https://titanic-api-880026336002.europe-west1.run.app/health

---

## Despliegue en la nube

El servicio está desplegado en **Google Cloud Run**, utilizando:

- Runtime de Python definido en `runtime.txt`  
- `Procfile` para indicar el comando de ejecución con Uvicorn  
- Integración con **Google Cloud Build**  

### URL del servicio (API LIVE)

https://titanic-api-880026336002.europe-west1.run.app

---

## Repositorio

https://github.com/alejandraveliz-crypto/titanic_api

---

## Equipo

- Alejandra Véliz  
- Juan Pablo Lucero  
- Leonor Saravia
