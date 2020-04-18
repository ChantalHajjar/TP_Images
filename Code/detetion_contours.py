from skimage import io
from matplotlib import pyplot as plt
from skimage.filters import sobel

im_cammen=io.imread('../images/cameraman.png')

sobel_cammen=sobel(im_cammen)

f,axes = plt.subplots(1, 2, figsize=(10, 10)) #pour afficher plusieurs graphiques sur la même ligne en spécifiant la taille des images

for ax in axes:
    ax.axis('off')  #masquer les axes de tous les graphiques  

(ax_c, ax_g) = axes
    
ax_c.imshow(im_cammen,cmap='gray')
ax_c.set_title('Image initiale')

ax_g.imshow(sobel_cammen,cmap='gray')
ax_g.set_title('Avec détection de contours')

f.show()
