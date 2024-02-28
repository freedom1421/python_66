import cv2
import os
import numpy as np
from PIL import Image

def assure_path_exists(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

recognizer = cv2.face.LBPHFaceRecognizer_create()

# Replace smart quotes with regular double quotes
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def getImagesAndLabels(path):
    # Get the current working directory
    current_dir = os.path.dirname(os.path.realpath(__file__))
    
    # Construct the full path to the 'dataset' directory
    full_path = os.path.join(current_dir, path)

    # Check if the directory exists
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"The specified path '{full_path}' does not exist.")

    imagePaths = [os.path.join(full_path, f) for f in os.listdir(full_path)]
    faceSamples = []
    ids = []

    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img, 'uint8')
        id_str = os.path.split(imagePath)[-1].split(".")[1]
        id = int(''.join(char for char in id_str if char.isdigit()))

        faces = detector.detectMultiScale(img_numpy)

        for (x, y, w, h) in faces:
            faceSamples.append(img_numpy[y:y+h, x:x+w])
            ids.append(id)

    return faceSamples, ids

try:
    faces, ids = getImagesAndLabels('dataset')
    # Continue with the rest of the code...
except FileNotFoundError as e:
    print(f"Error: {e}")