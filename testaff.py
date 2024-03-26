import numpy as np
import requests
import matplotlib.pyplot as pyplot
import matplotlib.image as mpimg
import sys
import datetime
from tensorflow import keras
from tensorflow.keras.models import Model
import tensorflow as tf
import cv2
import pathlib
import os
import zipfile
import tensorflow as tf
from tensorflow.keras.utils import plot_model
import csv

# Load the model from the HDF5 file
model = tf.keras.models.load_model('tensorboard.h5')

# Display model summary
print("Model Summary:")
model.summary()

# summarize filter shapes
for layer in model.layers:
    # check for convolutional layer
    if 'conv' not in layer.name:
        continue
    # get filter weights
    filters, biases = layer.get_weights()
    print(f"Layer Name: {layer.name}")
    print(f"Filter Shape: {filters.shape}")
    print("Filters:")
    print(filters)
    print("\n")

    # Write filters to a CSV file
    csv_file_name = f"{layer.name}_filters.csv"
    with open(csv_file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(filters)

# Function to read and display filter coefficients from CSV
def afficher_coefficients_filtres(chemin_fichier):
    with open(chemin_fichier, 'r') as fichier:
        lecteur_csv = csv.reader(fichier)
        for ligne in lecteur_csv:
            print(', '.join(ligne))  # Afficher les coefficients de manière lisible

# Appeler la fonction pour afficher les coefficients des filtres
# afficher_coefficients_filtres('conv2d_4_filters.csv')
