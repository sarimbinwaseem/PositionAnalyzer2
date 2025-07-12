import os
import sys

from PyQt6 import QtWidgets, uic, QtGui, QtCore

from FindingPosition import ReadFile, Analyze

# from save_thread_result import ThreadWithResult


class Ui(QtWidgets.QDialog):
    """UI functions of TOD Automatico"""

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(os.path.join("Program", "pa-main.ui"), self)
        self.setWindowTitle("Position Analyzer 2")
        self.setWindowIcon(
            QtGui.QIcon(os.path.join("Program", "positionanalyzerLogo.ico"))
        )

        self.browseButton.clicked.connect(self.browse)
        self.startButton.clicked.connect(self.startTheShow)
        # Check for existing result file
        pickle_path = os.path.join(os.getcwd(), "Result.pickle")
        if os.path.isfile(pickle_path):
            self.noteLabel.setText(
                'There is a result sheet loaded. No need to "Browse" again.'
            )
        else:
            pass

    def browse(self):

    	"""Browse pdf files for reading"""

        self.OnTopWaitLabel.setText(" Wait for a moment..Work in progress...")
        print("Getting The file path")
        self.file, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select PDF File", "", "PDF File (*.pdf)"
        )
        self.pdfPathInput.clear()

        if self.file is None:
            pass

        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.WaitCursor))
        self.startButton.setEnabled(False)

        self.read_pdf = ReadFile(self.file)
        self.read_pdf.error.connect(self.pdf_error)
        self.read_pdf.finished.connect(self.readingFinished)
        self.read_pdf.start()

        self.pdfPathInput.setText(self.file)
        # Check for existing result file

    def pdf_error(self, code):

    	"""Print error for pdf reading"""

        print(f"PDF ERROR: {code}")

    def readingFinished(self):

    	"""When pdf reading finishes"""

        print("Reading Done.")
        self.startButton.setEnabled(True)
        pickle_path = os.path.join(os.getcwd(), "Result.pickle")
        if os.path.isfile(pickle_path):
            self.noteLabel.setText("There is a result sheet loaded.")
        else:
            pass
        self.OnTopWaitLabel.setText("")
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))

    def startTheShow(self):

    	"""Starting number crunching on pdf data"""


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
        # tAnalyze = ThreadWithResult(target = self.analyze.run)
        self.analyze.result.connect(self.return_result)
        self.analyze.start()

    def return_result(self, result: list):

    	"""When pdf data is done analyzing"""

        self.done = result[0]
        print("Done")

        # Checking for wheteher to print all results or only student's
        if self.myResultCheck.isChecked():
            pass
        else:
            for i in self.done.results:
                self.allResultListWidget.addItem(i)
        # Making Position lines ready
        your_position = "Your Position is: " + str(self.done.position)
        students_ahead = "Students ahead you are: " + str(self.done.noOfNumber)

        # Printing Results
        self.yourResultListWidget.addItem(your_position)
        self.yourResultListWidget.addItem(students_ahead)
        # self.OnTopWaitLabel.setText("")

        # Converting cursor to normal condition
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.OnTopWaitLabel.setText(" Ready...")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec()
