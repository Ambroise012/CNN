import csv
import re
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from decimal import Decimal

# Fonction pour extraire les nombres d'une chaîne
def extract_decimal(s):
    numeric_part = re.search(r'[\d.]+', s)
    if numeric_part:
        return float(numeric_part.group())
    else:
        return None

# Ouvrir le fichier CSV en mode lecture
with open('conv2d_4_filters.csv', 'r') as csvfile:
    # Lire le fichier CSV
    csvreader = csv.reader(csvfile)
    
    # Ignorer l'en-tête s'il y en a un
    next(csvreader)
    
    # Initialiser des listes vides pour stocker les données
    x = []
    y = []
    z = []
    
    # Parcourir les lignes du fichier CSV et extraire les données
    for row in csvreader:
        # Vérifier si la ligne n'est pas vide
        if row:
            # Extraire les nombres de la ligne
            x_val = extract_decimal(row[0])
            y_val = extract_decimal(row[1])
            z_val = extract_decimal(row[2])
            
            # Vérifier si les valeurs extraites sont valides
            if x_val is not None and y_val is not None and z_val is not None:
                # Convertir les nombres décimaux en float
                x.append(float(x_val))
                y.append(float(y_val))
                z.append(float(z_val))

# Créer une nouvelle figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Tracer les points en 3D
ax.scatter(x, y, z)

# Étiqueter les axes
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# Afficher le graphique
plt.show()
