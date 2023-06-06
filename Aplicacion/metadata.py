import pandas as pd

path_data = 'models/categorias_iNat2021.txt'

# cargamos el fichero con las categorias
df = pd.read_csv(path_data, sep = '\t')

# devuelve el nombre común y la clasificación taxonómica
def render_prediction(prediction_idx):
    result = df.iloc[prediction_idx].to_json(orient="index")
    return result