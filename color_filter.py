from Tkinter import *
from PIL import Image, ImageTk
import numpy as np
import cv2



to_read = "foo1.jpg"
to_write = "bar.jpg"
top = Tk()


def button_call():
    apply_filter()
    global photo #
    original = Image.open(to_write)
    original.thumbnail(size,Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(original)#
    Image_canvas.itemconfigure(myimg, image=photo)#
    status.set("New Image")


def apply_filter():
	img = cv2.imread(to_read)
	to_set = [scale2.get(),scale1.get(),scale0.get()]#b,g,r
	for i  in range(0,img.shape[0]):
		#b= str(translate(i,0,img.shape[0],0,100))
		#b+=" % done"
		for j in range(0,img.shape[1]):
			for k in range(0,img.shape[2]):
				img.itemset((i,j,k),img.item(i,j,k)*to_set[k]/100)

	cv2.imwrite(to_write,img)


def translate(value, oldMin, oldMax, newMin, newMax):
    # Figure out how 'wide' each range is
    oldSpan = oldMax - oldMin
    newSpan = newMax - newMin

    # Convert the old range into a 0-1 range (float)
    valueScaled = float(value - oldMin) / float(oldSpan)

    # Convert the 0-1 range into a value in the new range.
    return newMin + (valueScaled * newSpan)
    

def color_change(x):
	value_slider = [translate(scale0.get(),0,100,0,255),translate(scale1.get(),0,100,0,255),translate(scale2.get(),0,100,0,255)]
	mycolor = '#%02x%02x%02x' % (value_slider[0],value_slider[1],value_slider[2])
	Color_canvas.configure(background=mycolor)





original = Image.open(to_read)
size = 355,int(355*float(original.size[1])/original.size[0])
original.thumbnail(size,Image.ANTIALIAS)
photo = ImageTk.PhotoImage(original)
Image_canvas = Canvas(top, bg="blue", height=original.size[1], width=original.size[0])
myimg = Image_canvas.create_image(size[0]/2, size[1]/2, image=photo)
Image_canvas.pack()



status = StringVar()
status_label = Label( top, textvariable=status )
status.set("Original Image")
status_label.pack()


Color_canvas = Canvas(top, bg="blue", height=30,width = 300)
Color_canvas.pack()


scale0 = Scale( top, orient=HORIZONTAL,length = 300,label = 'RED',command=color_change)
scale0.pack() 


scale1 = Scale( top, orient=HORIZONTAL,length = 300,label = 'GREEN',command=color_change)
scale1.pack()


scale2 = Scale( top, orient=HORIZONTAL,length = 300,label = 'BLUE',command=color_change)
scale2.pack()


Apply_button= Button(top, text ="Apply filter", command = button_call)
Apply_button.pack(side = BOTTOM,expand = TRUE)
top.mainloop()