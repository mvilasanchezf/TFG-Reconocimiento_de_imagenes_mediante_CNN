import torch
import torchvision.models as models
import torchvision.transforms as transforms
import PIL.Image as Image
import numpy as np

img_size = (224, 224)
mean = np.array([0.485, 0.456, 0.406])
std = np.array([0.229, 0.224, 0.225])
path_cnn = 'models/model.pth'

device = torch.device('cpu')
model = torch.load(path_cnn, map_location=device)
model.eval()

# Función que transforma la imagen en un tensor
def transform_image(infile):
    data_transform = transforms.Compose([
        transforms.Resize(img_size),
        transforms.ToTensor(),
        transforms.Normalize(mean, std)])
    # abre el fichero imagen
    image = Image.open(infile)
    # transforma la imagen en un tensor
    tensor_image = data_transform(image)
    # Crea un modelo de entrad por lotes con un solo elemento
    return tensor_image.unsqueeze(0)

# Función que realiza la prediccion
def get_prediction(input_tensor):
    # obtiene todas las probabilidades
    outputs = model.forward(input_tensor)
    # selecciona la clase con mayor probabilidad
    prob, classes = outputs.max(1)
    return prob.item(), classes.item()