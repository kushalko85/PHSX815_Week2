#! /usr/bin/env python

from Random import Random
import numpy as np
import matplotlib.pyplot as plt

random_number = Random(77777777)
myx = []

for x in range (1,10000):
    faces = random_number.Category6()
    myx.append(faces)


 # create histogram of our data
plt.figure()
plt.hist(myx ,6 , density=True, facecolor='green', histtype ="barstacked", alpha=0.75)

    # plot formating options
plt.xlabel('Dice faces')
plt.ylabel('Probability' , fontweight="bold" , fontsize="17")
plt.title('Categorical Distribution' , fontweight="bold" , fontsize="17")
plt.grid(True , color='r')


    # save and show figure
plt.savefig("Dice.png")
#plt.show()

# an array of rayleigh numbers using our Random class
myx = []
for i in range(0,10000):
    myx.append(random_number.Rayleigh())


# create histogram of our data
plt.figure()
plt.hist(myx, 70, density=True, facecolor='y', alpha=0.75)

# plot formating options
plt.xlabel('x')
plt.ylabel('Probability')
plt.title("Rayleigh Distribution",fontweight="bold")
plt.grid(True)

# show figure (program only ends once closed
plt.show()
plt.savefig("Rayleigh.png")

    
    
