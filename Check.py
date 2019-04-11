'''
c = "open Facebook"

if c.find("Open") != -1 or c.find("open") != -1:
	print ("found")

else:
	print("not found")


import os

file_name = "C:/Users/pankaj.kumar1/Desktop/PythonLib/SpeechFile/SpeechFile.mp3"

print (file_name)

'''

import sys
from PyQt4.QtGui import *
 
# Create an PyQT4 application object.
a = QApplication(sys.argv)
 
# The QWidget widget is the base class of all user interface objects in PyQt4.
w = QWidget()
 
# Set window size.
w.resize(320, 240)
 
# Set window title
w.setWindowTitle("Hello World!")
 
# Show window
w.show()
 
sys.exit(a.exec_())