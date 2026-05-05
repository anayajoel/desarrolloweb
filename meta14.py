from flask import Flask, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route("/")
def inicio():
    # ✅ Se agregaron dos alumnos más
    nombres = ["Ana", "Luis", "Carlos", "Sofía", "Pedro", "María"]
    calificaciones = np.array([85, 90, 78, 92, 70, 88])

    # Crear DataFrame
    df = pd.DataFrame({
        "nombre": nombres,
        "calificacion": calificaciones
    })

    # ✅ Nueva columna "estatus"
    df["estatus"] = df["calificacion"].apply(
        lambda x: "Aprobado" if x >= 80 else "Reprobado"
    )

    # Cálculos
    promedio = np.mean(calificaciones)
    maximo = np.max(calificaciones)
    
    # ✅ Calificación mínima
    minimo = np.min(calificaciones)

    # Convertir a diccionario
    datos = df.to_dict(orient="records")

    return render_template(
        "meta14.html",
        datos=datos,
        promedio=promedio,
        maximo=maximo,
        minimo=minimo
    )

if __name__ == "__main__":
    app.run(debug=True)