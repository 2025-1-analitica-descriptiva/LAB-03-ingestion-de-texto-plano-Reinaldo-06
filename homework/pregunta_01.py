"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import re

def pregunta_01():
    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    lines = lines[4:]

    data = []
    current_row = None

    for line in lines:
       
        if re.match(r"^\s+\d+\s{2,}", line):
            if current_row is not None:
                data.append(current_row)
            parts = re.split(r"\s{2,}", line.strip(), maxsplit=3)
            current_row = {
                "cluster": int(parts[0]),
                "cantidad_de_palabras_clave": int(parts[1]),
                "porcentaje_de_palabras_clave": float(parts[2].replace(",", ".").replace("%", "").strip()),
                "principales_palabras_clave": parts[3] if len(parts) > 3 else ""
            }
       
        elif current_row is not None:
            current_row["principales_palabras_clave"] += " " + line.strip()

    if current_row is not None:
        data.append(current_row)

    df = pd.DataFrame(data)

    # Normalizar columnas
    df.columns = [c.lower().replace(" ", "_") for c in df.columns]

    # Limpiar texto de palabras clave
    def limpiar_keywords(text):
        text = re.sub(r"\s+", " ", text.strip())  
        text = text.rstrip(".")  
        return ', '.join([kw.strip() for kw in text.split(',')]) 

    df["principales_palabras_clave"] = df["principales_palabras_clave"].apply(limpiar_keywords)

    return df

print(pregunta_01())