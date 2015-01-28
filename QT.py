#!/usr/bin/env python

#Encoding UTF-8
import sys
from PyQt4 import QtGui #getting the required imports, pretty standard

def main(): #Creating the 'main' function, this contains the code for the window widget
	app = QtGui.QApplication(sys.argv) #This is an application object (Located in QtGui module) the sys.argv is a list of parameter arguments from the cl

	window = QtGui.QWidget() #Base class for all UI objects in Qt4
	window.resize(250, 150) #Setting the size of said created window
	window.move(300, 300) #Telling it where to spawn on the screen
	window.setWindowTitle("Simple Window!") #Setting the window title, and if you didn't get that then you shouldn't be allowed near a computer!
	window.show() #makes the base class (The window) visable (and all the contained widgets i.e labels and buttons)

	sys.exit(app.exec_()) #this is just a mainloop of the app, the event handling starts from this point, the .exit() ensures a clean termination of the app

if __name__ == "__main__": #A standard python loop that runs the 'main' function
	main()