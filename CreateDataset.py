#import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import random
#import cv2
#Ensuite, on ouvre les deux images, background et l'image object
background = Image.open('D:/Test/files_for_test_pratique/background.png')
objet =  Image.open('D:/Test/files_for_test_pratique/object.png')

#image_object = cv2.imread('C:/Users/21266/Downloads/files_for_test_pratique/files_for_test_pratique/object.png')

#height, width, _ = image_object.shape
 
ii = 0
  
#j'ai pris 1000 comme taille
while(ii < 1000):
    #génrer une valeur aléatoire entre 0 et 4 pour voir le nombre de fois qu' on va mettre l'objet dans l'arrière plan
    nombre = random.randint(0,4)
    image_finale = background.copy()
    

    for item in range(nombre):
          
        x = random.randint(0,300)
        y = random.randint(0,300)
        #angle de la rotation de l'image aléatoire aussi
        rotation = random.randint(0,180)
        #On mets les images obtenues dans l'image d'origine 
        
        image_finale.paste(objet, (x, y))

   
    #Enregistrement avec la notation COCOii ou ii est un nombre qui s'incremente,
    # n'oubliez pas de préciser le chemin en fonction de votre PC et de vos repertoires 
    print(ii)
    im1 = image_finale.save("D:/Test/files_for_test_pratique/Dataset/0000" + str(ii) +".png")
    ii = ii + 1