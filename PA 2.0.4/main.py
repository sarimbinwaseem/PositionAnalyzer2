# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'positionanalyzer2.0.4.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import FindingPosition as fp
import os
import time
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 600)
        Dialog.setMinimumSize(QtCore.QSize(400, 600))
        Dialog.setMaximumSize(QtCore.QSize(400, 600))
        font = QtGui.QFont()
        font.setPointSize(8)
        Dialog.setFont(font)
        Dialog.setStyleSheet("")
        Dialog.setWindowIcon(QtGui.QIcon('positionanalyzerLogo.ico'))

        self.pdfPathInput = QtWidgets.QLineEdit(Dialog)
        self.pdfPathInput.setGeometry(QtCore.QRect(10, 84, 311, 31))
        self.pdfPathInput.setStyleSheet("border-style: solid;\n"
"border-radius: 3px;\n"
"border-color: royalblue;\n"
"border-width: 2px;")
        self.pdfPathInput.setObjectName("pdfPathInput")
        
        self.obtNumberInput = QtWidgets.QLineEdit(Dialog)
        self.obtNumberInput.setGeometry(QtCore.QRect(10, 167, 381, 31))
        self.obtNumberInput.setStyleSheet("border-style: solid;\n"
"border-radius: 3px;\n"
"border-color: royalblue;\n"
"border-width: 2px;")
        self.obtNumberInput.setObjectName("obtNumberInput")
        
        self.pdfPathLabel = QtWidgets.QLabel(Dialog)
        self.pdfPathLabel.setGeometry(QtCore.QRect(10, 61, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.pdfPathLabel.setFont(font)
        self.pdfPathLabel.setObjectName("pdfPathLabel")
        
        self.browseButton = QtWidgets.QToolButton(Dialog)
        self.browseButton.setGeometry(QtCore.QRect(330, 84, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(10)
        self.browseButton.setFont(font)
        self.browseButton.setStyleSheet("border-style: solid;\n"
"border-radius: 3px;\n"
"border-color: royalblue;\n"
"border-width: 2px;")
        self.browseButton.setObjectName("browseButton")
        self.browseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        self.obtnumberlabel = QtWidgets.QLabel(Dialog)
        self.obtnumberlabel.setGeometry(QtCore.QRect(10, 144, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.obtnumberlabel.setFont(font)
        self.obtnumberlabel.setObjectName("obtnumberlabel")
        
        self.startButton = QtWidgets.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(10, 237, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(16)
        self.startButton.setFont(font)
        self.startButton.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.startButton.setStyleSheet("border-style: solid;\n"
"border-radius: 3px;\n"
"border-color: royalblue;\n"
"border-width: 2px;")
        self.startButton.setObjectName("startButton")
        
        self.myResultCheck = QtWidgets.QCheckBox(Dialog)
        self.myResultCheck.setGeometry(QtCore.QRect(250, 209, 161, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(10)
        self.myResultCheck.setFont(font)
        self.myResultCheck.setObjectName("myResultCheck")
        
        self.allResultListWidget = QtWidgets.QListWidget(Dialog)
        self.allResultListWidget.setGeometry(QtCore.QRect(10, 295, 381, 211))
        self.allResultListWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.allResultListWidget.setStyleSheet("")
        self.allResultListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.allResultListWidget.setAutoScrollMargin(16)
        self.allResultListWidget.setObjectName("allResultListWidget")
        
        self.allResultsLabel = QtWidgets.QLabel(Dialog)
        self.allResultsLabel.setGeometry(QtCore.QRect(10, 275, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.allResultsLabel.setFont(font)
        self.allResultsLabel.setObjectName("allResultsLabel")
        
        self.yourResultLabel = QtWidgets.QLabel(Dialog)
        self.yourResultLabel.setGeometry(QtCore.QRect(10, 512, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.yourResultLabel.setFont(font)
        self.yourResultLabel.setObjectName("yourResultLabel")
        
        self.yourResultListWidget = QtWidgets.QListWidget(Dialog)
        self.yourResultListWidget.setGeometry(QtCore.QRect(10, 533, 381, 61))
        self.yourResultListWidget.setStyleSheet("border-style: solid;\n"
"border-radius: 3px;\n"
"border-color: royalblue;\n"
"border-width: 2px;")
        self.yourResultListWidget.setObjectName("yourResultListWidget")
        
        self.classComboBox = QtWidgets.QComboBox(Dialog)
        self.classComboBox.setGeometry(QtCore.QRect(130, 207, 101, 22))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.classComboBox.setFont(font)
        self.classComboBox.setStyleSheet("")
        self.classComboBox.setObjectName("classComboBox")
        self.classComboBox.addItem("XI")
        self.classComboBox.addItem("XII")
        
        self.selectClassLabel = QtWidgets.QLabel(Dialog)
        self.selectClassLabel.setGeometry(QtCore.QRect(10, 209, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.selectClassLabel.setFont(font)
        self.selectClassLabel.setObjectName("selectClassLabel")
        
        self.Note = QtWidgets.QLabel(Dialog)
        self.Note.setGeometry(QtCore.QRect(10, 123, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(10)
        self.Note.setFont(font)
        self.Note.setStyleSheet("color:green;")
        self.Note.setObjectName("Note")
        
        self.noteLabel = QtWidgets.QLabel(Dialog)
        self.noteLabel.setGeometry(QtCore.QRect(50, 120, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(11)
        # font.setBold(True)
        # font.setItalic(False)
        # font.setUnderline(False)
        # font.setWeight(50)
        # font.setKerning(False)
        self.noteLabel.setFont(font)
        self.noteLabel.setStyleSheet("color: green;")
        self.noteLabel.setText("")
        self.noteLabel.setObjectName("noteLabel")
        
        self.BlueFrame = QtWidgets.QFrame(Dialog)
        self.BlueFrame.setGeometry(QtCore.QRect(0, 0, 401, 51))
        self.BlueFrame.setStyleSheet("background-color: royalblue;")
        self.BlueFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BlueFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BlueFrame.setObjectName("BlueFrame")
        
        self.OnTopWaitLabel = QtWidgets.QLabel(self.BlueFrame)
        self.OnTopWaitLabel.setGeometry(QtCore.QRect(0, 0, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(19)
        self.OnTopWaitLabel.setFont(font)
        # self.OnTopWaitLabel.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.OnTopWaitLabel.setStyleSheet("color: white;")
        self.OnTopWaitLabel.setObjectName("OnTopWaitLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.browseButton.clicked.connect(self.browse)
        self.startButton.clicked.connect(self.startTheShow)
        # Check for existing result file
        picklePath = os.path.join(os.getcwd(), "Result.pickle")
        if os.path.isfile(picklePath):
        	self.noteLabel.setText('There is a result sheet loaded. No need to "Browse" again.')
        else:
        	pass

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Position Analyzer 2"))
        self.pdfPathInput.setToolTip(_translate("Dialog", "Enter PDF File path of result"))
        self.obtNumberInput.setToolTip(_translate("Dialog", "Enter Your Obtained Number "))
        self.pdfPathLabel.setText(_translate("Dialog", "Enter PDF Path:"))
        self.browseButton.setToolTip(_translate("Dialog", "Browse PDF File of Result"))
        self.browseButton.setText(_translate("Dialog", "Browse"))
        self.obtnumberlabel.setText(_translate("Dialog", "Enter Your Obtained Number:"))
        self.startButton.setText(_translate("Dialog", "START"))
        self.myResultCheck.setToolTip(_translate("Dialog", "This will display only your result"))
        self.myResultCheck.setText(_translate("Dialog", "Display My Result Only"))
        self.allResultsLabel.setText(_translate("Dialog", "All Results:"))
        self.yourResultLabel.setText(_translate("Dialog", "Your Result:"))
        self.classComboBox.setToolTip(_translate("Dialog", "Select Your Class/Grade"))
        self.selectClassLabel.setText(_translate("Dialog", "Select Your Class:"))
        self.Note.setText(_translate("Dialog", "NOTE:"))
        self.OnTopWaitLabel.setText(_translate("Dialog", " Ready..."))

    def browse(self):
    	self.OnTopWaitLabel.setText(" Wait for a moment..Work in progress...")
    	print("Getting The file path")
    	self.file, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select PDF File", "", "PDF File (*.pdf)")
    	path = self.file
    	self.pdfPathInput.clear()
    	fp.importingFile(self.file)
    	self.pdfPathInput.setText(path)
    	# Check for existing result file
    	picklePath = os.path.join(os.getcwd(), "Result.pickle")
    	if os.path.isfile(picklePath):
    		self.noteLabel.setText('There is a result sheet loaded. No need to "Browse" again.')
    	else:
    		pass
    	self.OnTopWaitLabel.setText("")

    def startTheShow(self):
    	
    	self.OnTopWaitLabel.setText("")

    	self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))

    	print("Start button pressed")
    	time.sleep(0.5)
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
    	done = fp.check(int(obtMarksNum), int(totalNumbers))
    	print("Done")
    	# Extracting Data From Main Function
    	results = done[0]
    	position = done[1]
    	noOfNumber = done[2]
    	# Checking for wheteher to print all results or onlt student's
    	if self.myResultCheck.isChecked():
    		pass
    	else:
    		for i in results:
    			self.allResultListWidget.addItem(i)
    	# Making Position lines ready
    	positionn = "Your Position is: " + str(position)
    	noOfNumberr = "Students ahead you are: " + str(noOfNumber)

    	# Printing Results
    	self.yourResultListWidget.addItem(positionn)
    	self.yourResultListWidget.addItem(noOfNumberr)
    	# self.OnTopWaitLabel.setText("")
    	
    	# Converting cursor to normal condition 
    	self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
    	time.sleep(0.5)
    	# self.OnTopWaitLabel.setText(" Ready...")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())