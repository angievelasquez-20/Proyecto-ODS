from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    try:
        df = pd.read_csv("AFECTACI_N_DE_MIEMBROS_DE_LA_FUERZA_P_BLICA_20250510 (1).cvs")
        datos = df.to_dict(orient='records')  # Convertir DataFrame a lista de diccionarios
        return render_template('index.html', data=datos)
    except FileNotFoundError:
        return "Error: No se encontró el archivo de datos (afectaciones_fuerza_publica.csv).  Asegúrate de ejecutar obtener_datos.py primero.", 404

if __name__ == '__main__':
    app.run(debug=True)