from skimage import io
from matplotlib import pyplot as plt
from skimage.filters import sobel

im_camman=io.imread('../images/cameraman.png')

sobel_camman=sobel(im_camman)

f,axes = plt.subplots(1, 2, figsize=(10, 10)) #pour afficher plusieurs graphiques sur la même ligne en spécifiant la taille des images

for ax in axes:
    ax.axis('off')  #masquer les axes de tous les graphiques  

(ax_c, ax_g) = axes
    
ax_c.imshow(im_camman,cmap='gray')
ax_c.set_title('Image initiale')

ax_g.imshow(sobel_camman,cmap='gray')
ax_g.set_title('Avec détection de contours')

f.show()
