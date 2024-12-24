import pandas as pd
import streamlit as st


def remove_code():
    # Cargar el archivo CSV
    df = pd.read_csv('data/codes.csv')

    # Verificar si hay códigos disponibles
    if df.empty:
        return None

    # Obtener el primer código
    code = df.iloc[0]['code']

    # Eliminar el primer código del DataFrame
    df = df.iloc[1:]

    # Guardar el DataFrame actualizado de nuevo en el archivo CSV
    df.to_csv('data/codes.csv', index=False)

    

    return code


def remove_code_cloud():
    # Leer el contenido del archivo 'codes.csv' desde los secretos
    codes_csv_content = st.secrets["codes"]["CODES_CSV"]
    with open('data/codes.csv', 'w') as f:
        f.write(codes_csv_content)

    # Cargar el archivo CSV
    df = pd.read_csv('data/codes.csv', header=None, names=['code', 'description'])

    # Verificar si hay códigos disponibles
    if df.empty:
        return None

    # Obtener el primer código
    code = df.iloc[0]['code']

    # Eliminar el primer código del DataFrame
    df = df.iloc[1:]

    # Guardar el DataFrame actualizado de nuevo en el archivo CSV
    df.to_csv('data/codes.csv', index=False, header=False)

    return code