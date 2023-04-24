import sys, os
from PyQt6 import QtWidgets, uic, QtGui, QtCore
from FindingPosition import ReadFile, Analyze
from save_thread_result import ThreadWithResult

class Ui(QtWidgets.QDialog):
	'''UI functions of TOD Automatico'''
	def __init__(self):
		super(Ui, self).__init__()
		uic.loadUi(os.path.join("Program", "pa-main.ui"), self)
		self.setWindowTitle("Position Analyzer 2")
		self.setWindowIcon(QtGui.QIcon(os.path.join("Program", "positionanalyzerLogo.ico")))

		self.browseButton.clicked.connect(self.browse)
		self.startButton.clicked.connect(self.startTheShow)
		# Check for existing result file
		picklePath = os.path.join(os.getcwd(), "Result.pickle")
		if os.path.isfile(picklePath):
			self.noteLabel.setText('There is a result sheet loaded. No need to "Browse" again.')
		else:
			pass

	def browse(self):
		self.OnTopWaitLabel.setText(" Wait for a moment..Work in progress...")
		print("Getting The file path")
		self.file, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select PDF File", "", "PDF File (*.pdf)")
		self.pdfPathInput.clear()
		
		if self.file is None:
			pass
		
		self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.WaitCursor))
		self.startButton.setEnabled(False)

		self.readPDF = ReadFile(self.file)
		self.readPDF.error.connect(self.pdf_error)
		self.readPDF.finished.connect(self.readingFinished)
		self.readPDF.start()

		self.pdfPathInput.setText(self.file)
		# Check for existing result file


	def pdf_error(self, code):
		print(f"PDF ERROR: {code}")

	def readingFinished(self):
		print("Reading Done.")
		self.startButton.setEnabled(True)
		picklePath = os.path.join(os.getcwd(), "Result.pickle")
		if os.path.isfile(picklePath):
			self.noteLabel.setText('There is a result sheet loaded.')
		else:
			pass
		self.OnTopWaitLabel.setText("")
		self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))

	def startTheShow(self):
		
		self.OnTopWaitLabel.setText("Working...")

		self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.WaitCursor))

		print("Start button pressed")
		
		# Clearing The Result Widget
		self.yourResultListWidget.clear()
		self.allResultListWidget.clear()
		
		# Obtaining Obtained Marks
		obtMarksNum = self.obtNumberInput.text()

		# Checking for Academic Class 
		tu = self.classComboBox.currentText()
		if tu == "XI":
			totalNumbers = 550
		else:
			totalNumbers = 1100

		print("Starting check")
		# Executing Main Function
		self.analyze = Analyze(int(obtMarksNum), int(totalNumbers))
		tAnalyze = ThreadWithResult(target = self.analyze.run)
		tAnalyze.start()
		tAnalyze.join()

	# def backed_result(self, result):
		self.done = tAnalyze.result
		print("Done")

		# Checking for wheteher to print all results or only student's
		if self.myResultCheck.isChecked():
			pass
		else:
			for i in self.done.results:
				self.allResultListWidget.addItem(i)
		# Making Position lines ready
		positionn = "Your Position is: " + str(self.done.position)
		noOfNumberr = "Students ahead you are: " + str(self.done.noOfNumber)

		# Printing Results
		self.yourResultListWidget.addItem(positionn)
		self.yourResultListWidget.addItem(noOfNumberr)
		# self.OnTopWaitLabel.setText("")
		
		# Converting cursor to normal condition 
		self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
		self.OnTopWaitLabel.setText(" Ready...")



if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = Ui()
	window.show()
	app.exec()