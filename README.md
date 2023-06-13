# (ESP) Reconocimiento de imágenes mediante aprendizaje profundo 

![](https://github.com/mvilasanchezf/TFG-Reconocimiento_de_imagenes_mediante_CNN/blob/master/assets/Arquitectura%20TFG%20small.png)

Este proyecto es mi trabajo de fin de grado para el ciclo de desarrollo de aplicaciones multiplataforma.
 
 Consta de dos partes diferenciadas:
 * El código desarrollado en cuadernos de Jupyter para el entrenamiento de diferentes modelos de redes neuronales convolucionales (CNN) para la clasificación de imágenes.
 * Una aplicación desarrollada en Flask, que realiza una predicción de que especie se trata el ser vivo (animales, hongos ó plantas) que contiene la fotografía que se le pasa como entrada. Esta aplicación utiliza el modelo de CNN que mejor rendimiento ha obtenido en los cuadernos de Jupyter. 
 * Extra: La propia memoria del proyecto, que se encuentra en formato PDF. Junto con una demostración de la aplicación en formato vídeo. 

## Descripción de los cuadernos de Jupyter

Los cuadernos de Jupyter se encuentran en la carpeta "Cuadernos CNN". En ellos se encuentra el código desarrollado para el entrenamiento de los modelos de CNN.

### Cuadernos de Jupyter

* **1.0 - Preparación de los datos:** Se realiza un analisis de los datos previos al entrenamiento de los modelos. Se realiza la carga de los datos, se realiza un analisis exploratorio de los datos, se realiza un preprocesamiento de los metadatos almacenados en un fichero json y se guardan los datos en formato .csv para su posterior uso en la prueba de concepto.

* **2.0 - Entrenamiento de los modelos:** Se realiza el entrenamiento de los modelos de CNN. Se cargan los datos, se cargan los modelos, se realiza el entrenamiento de los modelos y se guardan los modelos entrenados en formato .pth para su posterior uso en la aplicación. Y se guardan los resultados del entrenamiento en formato .csv para su posterior uso en la evaluación de los modelos.

* **3.0 - Evaluación de los modelos:** Se realiza la evaluación de los modelos de CNN. Se cargan los resultados del entrenamiento, se analizan y se generan las gráficas de los resultados en formato .jpg para su posterior uso en la memoria del proyecto.

* **4.0 - Comparación de los modelos:** Se realiza la comparación de los 3 mejores resultados de los modelos de CNN. Generando una unica gráfica con los resultados de los 3 modelos en formato .jpg para su posterior uso en la memoria del proyecto.

* **5.0 - Ejemplo de convolución:** Se realiza un ejemplo de convolución de una imagen a la que se le aplican sucessivamente diferentes filtros para obtener diferentes mapas de características. Las imágenes resultantes se guardan en formato .jpg para su posterior uso en la presentacion para la defensa del proyecto. 


## Descripción de la aplicación

La aplicación se encuentra en la carpeta "Aplicación". En ella se encuentra el código desarrollado para la aplicación web.

### Aplicación

* **app.py:** Se encuentra el core del código de la aplicación web desarrollada en Flask. Llamama al modelo de CNN entrenado, se carga la imagen de entrada, se realiza la predicción de la imagen y se muestra el resultado en la página web.

* **cnn.py:** Se encuentra el código de la clase CNN, que se encarga de cargar el modelo de CNN entrenado y realizar la predicción de la imagen de entrada.

* **metadata.py:** Se encuentra el código de la clase Metadata, que se encarga de cargar los metadatos de las especies de animales, hongos y plantas, y de realizar la predicción de la imagen de entrada.

* **templates:** Se encuentra el código html de la página web de la aplicación.

* **static:** Se encuentra el código css de la página web de la aplicación y las imágenes estaticas de la página web.

* **modelos:** Se encuentra el modelo de CNN entrenado y los metadatos de las especies de animales, hongos y plantas.



## Instalación de los requisitos previos para la ejecución del código

Para poder ejecutar el código de los cuadernos de Jupyter, es necesario tener instalado Python 3.11 o superior, y las siguientes librerías:

```sh
pip install pytorch
pip install torchvision
pip install numpy
pip install matplotlib
pip install pandas


```

Para poder ejecutar la aplicación, es necesario tener instalado Python 3.11 o superior, y las siguientes librerías:

```sh
pip install flask
pip install pandas
pip install torch
pip install torchvision
pip install numpy

```

# (ENG) Image recognition through deep learning

This project is my final degree project for the multiplatform application development cycle.

It consists of two differentiated parts:
* The code developed in Jupyter notebooks for the training of different convolutional neural network (CNN) models for image classification.
* An application developed in Flask, which makes a prediction of which species is the living being (animals, fungi or plants) that contains the photograph that is passed as input. This application uses the CNN model that has obtained the best performance in the Jupyter notebooks.
* Extra: The project's own memory, which is in PDF format. Along with a demonstration of the application in video format.

## Description of Jupyter notebooks

The Jupyter notebooks are located in the "Cuadernos CNN" folder. In them is the code developed for the training of CNN models.

### Jupyter notebooks

* **1.0 - Data preparation:** An analysis of the data prior to the training of the models is carried out. The data is loaded, an exploratory analysis of the data is carried out, a preprocessing of the metadata stored in a json file is carried out and the data is saved in .csv format for later use in the proof of concept.

* **2.0 - Training of the models:** The training of the CNN models is carried out. The data is loaded, the models are loaded, the models are trained and the trained models are saved in .pth format for later use in the application. And the results of the training are saved in .csv format for later use in the evaluation of the models.

* **3.0 - Evaluation of the models:** The evaluation of the CNN models is carried out. The training results are loaded, analyzed and the results graphs are generated in .jpg format for later use in the project report.

* **4.0 - Comparison of the models:** The comparison of the 3 best results of the CNN models is carried out. Generating a single graph with the results of the 3 models in .jpg format for later use in the project report.

* **5.0 - Convolution example:** An example of convolution of an image is performed to which different filters are applied successively to obtain different feature maps. The resulting images are saved in .jpg format for later use in the presentation for the defense of the project.


## Description of the application

The application is located in the "Aplicación" folder. In it is the code developed for the web application.

### Application

* **app.py:** The core of the code of the web application developed in Flask is located. It calls the trained CNN model, loads the input image, makes the prediction of the image and shows the result on the web page.

* **cnn.py:** The code of the CNN class is located, which is responsible for loading the trained CNN model and making the prediction of the input image.

* **metadata.py:** The code of the Metadata class is located, which is responsible for loading the metadata of the animal, fungi and plant species, and for making the prediction of the input image.

* **templates:** The html code of the web page of the application is located.

* **static:** The css code of the web page of the application and the static images of the web page are located.

* **modelos:** The trained CNN model and the metadata of the animal, fungi and plant species are located.



## Installation of the prerequisites for running the code

In order to run the code of the Jupyter notebooks, it is necessary to have Python 3.11 or higher installed, and the following libraries:

```sh
pip install pytorch
pip install torchvision
pip install numpy
pip install matplotlib
pip install pandas


```

In order to run the application, it is necessary to have Python 3.11 or higher installed, and the following libraries:

```sh
pip install flask
pip install pandas
pip install torch
pip install torchvision
pip install numpy

```
