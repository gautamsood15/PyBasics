import pyqrcode
import os, shutil

title = input("Give your QR code a title! >> ")
text = input("What would you like your QR code to say? ")

file_name_svg = title + ".svg"
file_name_png = title + ".png"

url = pyqrcode.create(text)

url.svg(file_name_svg, scale=8)
url.png(file_name_svg, scale=10)

os.mkdir(fr"/home/gautam/Desktop/Py_Basics/Py_QR/{title}")

shutil.move(f"{file_name_png}", fr"/home/gautam/Desktop/Py_Basics/Py_QR/{title}")
shutil.move(f"{file_name_svg}", fr"/home/gautam/Desktop/Py_Basics/Py_QR/{title}")





