"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    import pandas as pd

    # Cargar el archivo de texto en un DataFrame
    df = pd.read_csv('files/input/clusters_report.txt', sep='\t')

    # Renombrar las columnas a minúsculas y reemplazar espacios por guiones bajos
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # Separar las palabras clave por coma y un espacio
    df['palabras_clave'] = df['palabras_clave'].str.replace(', ', ',')

    return df

print(pregunta_01().head())