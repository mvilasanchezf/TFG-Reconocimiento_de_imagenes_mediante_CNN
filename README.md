## Reconocimiento de imágenes mediante aprendizaje profundo

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

Para poder ejecutar el código de los cuadernos de Jupyter, es necesario tener instalado Python 3.6 o superior, y las siguientes librerías:

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
