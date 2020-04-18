import numpy as np
from skimage import io
from matplotlib import pyplot as plt
from skimage import color
from skimage.filters import threshold_otsu
from skimage.measure import label,regionprops

im_stars=io.imread('../images/stars.jpg')
im_stars_gray=color.rgb2gray(im_stars) #transformer l'image en niveaux de gris
thresh = threshold_otsu(im_stars_gray) #appliquer le seuillage de Otsu
im_stars_binary = im_stars_gray >thresh #générer l'image binaire

label_img = label(im_stars_binary) 
regions = regionprops(label_img)      #détecter les objets formés par les pixels blancs (les étoiles)
print("Nombre d'objets d'étoiles:",len(regions))

f,axes = plt.subplots(2, 2,figsize=(20, 10)) #pour afficher 4 graphiques sur deux lignes

for lig in axes:
  for ax in lig: 
      ax.axis('off')  #masquer les axes de tous les graphiques  

((ax1,ax2),(ax3,ax4)) = axes

ax1.imshow(im_stars, cmap='gray')
ax1.set_title('Image initiale')

ax2.imshow(im_stars_gray, cmap='gray')
ax2.set_title('Image en niveaux de gris')

ax3.imshow(im_stars_binary, cmap='gray')
ax3.set_title('Image binaire')

ax4.imshow(im_stars_binary, cmap='gray')
ax4.set_title('Image binaire avec identification des objets')
for props in regions:
    y0, x0 = props.centroid
    ax4.plot(x0, y0, '.r', markersize=2) #afficher des points rouges au centre des objets détectés
f.show()
