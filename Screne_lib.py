
import os
import pyscreenshot as ImageGrab

my_list = os.listdir('/tmp/')

im = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
im.show()

my_list_2 = os.listdir('/tmp/')

scr_name=list(set(my_list_2)-set(my_list))[0]
print(scr_name)

print("end sicle")