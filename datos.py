import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
import datos  # Importar el archivo datos.py

# Cargar el dataset
df = datos.cargar_datos('data/ods.csv')
if df is not None:
    # Preprocesamiento
    df = datos.limpiar_datos(df)
    df = datos.crear_caracteristicas(df)
    df, le_dep, le_evt = datos.codificar_variables(df) # Guardar los LabelEncoders

    # Definir variables
    X = df[['Departamento', 'Mes', 'Año', 'Tipo de evento']]
    y = df['Resultado'].apply(lambda x: 1 if 'herido' in x.lower() or 'muerto' in x.lower() else 0)

    # Entrenar modelo
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Guardar modelo y codificadores
    joblib.dump(model, 'modelo_riesgo.pkl')
    joblib.dump(le_dep, 'le_dep.pkl')
    joblib.dump(le_evt, 'le_evt.pkl')
    print("Modelo entrenado y guardado.")
else:
    print("No se pudo cargar el dataset.")