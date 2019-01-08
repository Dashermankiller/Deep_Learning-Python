from sklearn import tree
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# 1== Smooth
# 0== bumpy
features =[[140,1],[130,1],[150,0],[170,0]]
labels=[0,0,1,1]
clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)
lb=int(input("LB: "))
a=int(input("Smooth: "))
prediction=clf.predict([[lb,a]])
if prediction ==0:
    img=mpimg.imread('Apple.jpg')
    imgplot = plt.imshow(img)
    plt.show()
elif prediction==1:
    img=mpimg.imread('Orange.jpg')
    imgplot = plt.imshow(img)
    plt.show()

# 1 == Orange
# 0== Apple