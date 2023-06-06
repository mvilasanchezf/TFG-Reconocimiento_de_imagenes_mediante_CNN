from flask import Flask, request , render_template 
from cnn import transform_image, get_prediction
from metadata import render_prediction
import json
from PIL import Image

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['fileToUpload']
        if file is not None:
            input_tensor = transform_image(file)
            predict_prob, prediction_idx = get_prediction(input_tensor)
            class_name = render_prediction(prediction_idx)
            image = Image.open(file)

            #parseamos el json class_name para devolver las categorias de la imagen almacenadas en el json pasandolos a strings
            details = json.loads(class_name)
            common_name = details["common_name"]
            kingdom = details["kingdom"]
            phylum = details["phylum"]
            class_ = details["class"]
            order = details["order"]
            family = details["family"]
            genus = details["genus"]
            specific_epithet = details["specific_epithet"]

            response = {'prediction': {'accuracy': predict_prob, 'common_name': common_name, 'kingdom': kingdom, 'phylum': phylum, 'class': class_, 'order': order, 'family': family, 'genus': genus, 'specific_epithet': specific_epithet}}
            return render_template('index.html', 
                                    user_image = file,
                                    prediction_text = "Con una precisión del {0} '%' ".format(response["prediction"]["accuracy"]), 
                                    prediction_text2 =  " El Nombre comun es: {0}".format(response["prediction"]["common_name"]),
                                    prediction_text3 =  " El reino es: {0}".format(response["prediction"]["kingdom"]),
                                    prediction_text4 =  " El phylum es: {0}".format(response["prediction"]["phylum"]),
                                    prediction_text5 =  " La clase es: {0}".format(response["prediction"]["class"]),
                                    prediction_text6 =  " El orden es: {0}".format(response["prediction"]["order"]),
                                    prediction_text7 =  " La familia es: {0}".format(response["prediction"]["family"]),
                                    prediction_text8 =  " El genero es: {0}".format(response["prediction"]["genus"]),
                                    prediction_text9 =  " La especie es: {0}".format(response["prediction"]["specific_epithet"])
                                    )
                                     

if __name__ == '__main__':
    app.run(debug=True)
