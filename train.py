import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib


# 1. Cargar datos
df = pd.read_csv("train.csv")

# 2. Columnas
cols_features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]
target = "Survived"

df = df[cols_features + [target]]

# 3. Limpieza mínima
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Fare"] = df["Fare"].fillna(df["Fare"].median())
df["Sex"] = df["Sex"].map({"female": 0, "male": 1})

# 4. Definir X e y
X = df[cols_features]
y = df[target]

# 5. Train / Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6. Modelo (Regresión Logística simple)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 7. Predicción y métrica
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy en test: {acc:.3f}")

# 8. Guardar el modelo entrenado en un archivo .pkl
joblib.dump(model, "regresion_logistica_titanic.pkl")
print("Modelo guardado en .pkl")