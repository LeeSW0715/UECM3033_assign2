import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy as sp

def image_svd(n):
    Sr1=Sr.copy()
    Sg1=Sg.copy()
    Sb1=Sb.copy()

    Sr1[n:800]=np.zeros_like(Sr[n:800])
    Sg1[n:800]=np.zeros_like(Sg[n:800])
    Sb1[n:800]=np.zeros_like(Sb[n:800])

    Sr1 = sp.linalg.diagsvd(Sr1,800,1000)
    Sg1 = sp.linalg.diagsvd(Sg1,800,1000)
    Sb1 = sp.linalg.diagsvd(Sb1,800,1000)

    new_r = np.dot(np.dot(Ur,Sr1), Vr)
    new_g = np.dot(np.dot(Ug,Sg1), Vg)
    new_b = np.dot(np.dot(Ub,Sb1), Vb) 

    img[:,:,0]= new_r
    img[:,:,1]= new_g
    img[:,:,2]= new_b

    #to plot the images
    fig2 = plt.figure(n)
    ax1 = fig2.add_subplot(2,2,1)
    ax2 = fig2.add_subplot(2,2,2)
    ax3 = fig2.add_subplot(2,2,3)
    ax4 = fig2.add_subplot(2,2,4)
    ax1.imshow(img)
    ax2.imshow(r, cmap = 'Reds')
    ax3.imshow(g, cmap = 'Greens')
    ax4.imshow(b, cmap = 'Blues')
    plt.show()

img=mpimg.imread('Nikon.JPG')
[r,g,b] = [img[:,:,i] for i in range(3)]

fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(r, cmap = 'Reds')
ax3.imshow(g, cmap = 'Greens')
ax4.imshow(b, cmap = 'Blues')
plt.show()

U, s, V = np.linalg.svd(r, full_matrices=True)
print(U.shape)
print( V.shape)
print(s.shape)

#to find U, sigma and V for red , green, and blue matrix
Ur, Sr, Vr = sp.linalg.svd(r) 
Ug, Sg, Vg = sp.linalg.svd(g) 
Ub, Sb, Vb = sp.linalg.svd(b) 

#to find the none zero elements in sigma of each red, green, and blue matrices
nonzero_r=np.count_nonzero(Sr)
nonzero_g=np.count_nonzero(Sg)
nonzero_b=np.count_nonzero(Sb)
print("Non-zero elements in matrices are", nonzero_r,"," ,nonzero_g,"and" ,nonzero_b, ".")

#lower resolution of sigma 30
image_svd(30)

#better resolution of sigma 200
image_svd(200)
