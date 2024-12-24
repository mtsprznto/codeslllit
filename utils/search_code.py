import pandas as pd

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

