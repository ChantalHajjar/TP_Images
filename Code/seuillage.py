from skimage import io
from matplotlib import pyplot as plt
from skimage.filters import threshold_otsu

im_cammen=io.imread('../images/cameraman.png')
thresh = threshold_otsu(im_cammen)
binary = im_cammen > thresh

f,axes = plt.subplots(1, 2, figsize=(10, 10)) #pour afficher plusieurs graphiques sur la même ligne en spécifiant la taille des images

for ax in axes:
    ax.axis('off')  #masquer les axes de tous les graphiques  

(ax_c, ax_b) = axes
    
ax_c.imshow(im_cammen,cmap='gray')
ax_c.set_title('Image intiale')

ax_b.imshow(binary,cmap='gray')
ax_b.set_title('Image binaire')
f.show()
