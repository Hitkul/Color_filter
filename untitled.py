import numpy as np
import cv2
import sys


def translate(value, oldMin, oldMax, newMin, newMax):
    # Figure out how 'wide' each range is
    oldSpan = oldMax - oldMin
    newSpan = newMax - newMin

    # Convert the old range into a 0-1 range (float)
    valueScaled = float(value - oldMin) / float(oldSpan)

    # Convert the 0-1 range into a value in the new range.
    return newMin + (valueScaled * newSpan)

# Load an color image in grayscale
print " Reading the image"
img = cv2.imread('foo.jpg')
to_set = [60,20,30]#b,g,r
print "Applying color filter"
for i  in range(0,img.shape[0]):
	#print 
	b= str(translate(i,0,img.shape[0],0,100))
	b+=" % done"
	sys.stdout.write('\r'+b)
	for j in range(0,img.shape[1]):
		for k in range(0,img.shape[2]):
			img.itemset((i,j,k),img.item(i,j,k)*to_set[k]/100)

print " "
cv2.imwrite('bar.jpg',img)

