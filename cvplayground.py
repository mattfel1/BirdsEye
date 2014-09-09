import numpy as np
from copy import deepcopy
import cv2

# mouse callback function
def get_point(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),1,(255,0,0),-1)
        print x,y

def scale_output_square(factor,points):
	newpoints = deepcopy(points)
	avg_x = (points[0][0] + points[1][0] + points[2][0] + points[3][0])/4
	avg_y = (points[0][1] + points[1][1] + points[2][1] + points[3][1])/4
	for n in range(0,4):
		newpoints[n][0] = avg_x - (avg_x - points[n][0])*factor
		newpoints[n][1] = avg_y - (avg_y - points[n][1])*factor
	return newpoints

img_location = 'course.jpeg'
img = cv2.imread(img_location)
rows,cols,ch = img.shape
print rows, cols, ch

cv2.namedWindow('image')
cv2.setMouseCallback('image',get_point)
#cv2.waitKey(0)

#help me find the coners of the square
for n in range(493,794):
 	print (img[481,n])
 	img[481,n] = (0,255,0)
 	print n
print "NEEEEEXT\n\n\n\n\n\n\n"
for n in range(486,698):
 	print (img[457,n])
 	img[457,n] = (0,255,0)
 	print n

#calculate xform matrix
orig = np.float32([[556,481],[509,457],[783,481],[669,457]])
#assuming square is 227px big
guess = np.float32([[556,481],[556,254],[783,481],[783,254]])
new = scale_output_square(.4,guess)
print new

M = cv2.getPerspectiveTransform(orig,new)

imgx = cv2.warpPerspective(img,M,(800,800))
cv2.imwrite('xformed.png',imgx)
print M

while(1):
    cv2.imshow('image',img)
    cv2.imshow('xformed',imgx)


    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()