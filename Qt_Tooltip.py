import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
	def __init__(self):
		super(Example, self).__init__()

		self.initUI()

	def initUI(self):

		QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10)) #Static method, sets a font used to render tooltips. We use a 10px SansSerif

		self.setToolTip("This is a <b>QWidget</b> widget") #To create a tooltpip we call the 'setTooltip()' method, we can slso use rich text formatting

		button = QtGui.QPushButton("Button", self) #Simply creating the button...
		button.setToolTip("This is a <b>QPushButton</b> widget") #...and adding a tooltip for it
		button.resize(button.sizeHint()) #The button is being resized and moved on the window. the 'sizeHint()' method gives a recommended size for the button
		button.move(50,50)

		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle("ToolTips")
		self.show()

def main():
	app = QtGui.QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()

