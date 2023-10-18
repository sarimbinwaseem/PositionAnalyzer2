import PyPDF2 
import os
import pickle
from PyQt6.QtCore import QThread, pyqtSignal
from result import Result

class ReadFile(QThread):

	error = pyqtSignal(int)

	def  __init__(self, filePath: str):
		super().__init__()
		self.filePath = filePath

	def run(self):

		try:
			# with open(self.filePath, 'rb') as pdfRawFile: 
			pdfReader = PyPDF2.PdfReader(self.filePath)

		except OSError:
			self.error.emit(-1)
			
		except FileNotFoundError:
			self.error.emit(-2)

		except Exception as e:
			print(e)
			self.error.emit(-3)
		else:  


			# printing number of pages in pdf file 
			pages  = len(pdfReader.pages)
			# print(type(pdfReader.pages))
			totalpages = f"Total number of pages in PDF: {pages}"
			
			extracted_text = []

			with open("Result.pickle", "wb") as R_txt:
				for i in range(pages): 	
					# creating a page object 
					pageObj = pdfReader.pages[i]  
					text = pageObj.extract_text()
					extracted_text.append(text)

				pickle.dump(extracted_text, R_txt)

class Analyze:

	def __init__(self, obtMarksNum: int, totalNumbers: int):

		super().__init__()

		self.obtMarksNum = obtMarksNum
		self.totalNumbers = totalNumbers

	def run(self):
		
		result = Result()

		line = "1 ahead........"
		numb  = []
		# pickle_obj = []
		# path = os.path.join(os.getcwd(), "Result.pickle")
		
		with open("Result.pickle", "rb") as file:
			pickle_obj = pickle.load(file)

		words = []
		for w in pickle_obj:
			words.append(w.split())
			# print(words)

		for number in range(self.obtMarksNum + 1, self.totalNumbers):
			toSearch1 = "(" + str(number) + ")"
			toSearch2 = "(" + str(number) + "+" 
			toSearch3 = "(" + str(number) + "^"


			for worde in words:
				# print(word)
				for word in worde:
					if word.find(toSearch1) != -1 or word.find(toSearch2) != -1 or word.find(toSearch3) != -1:
						output = str(line) + " Scoring: "+ str(number) + " having " + str(round(((number/self.totalNumbers)*100),2)) + ' %.'
						# print(output)
						result.results.append(output)
						line = "1 more ahead..."
						result.noOfNumber += 1
						if number in numb:
							pass
						else:
							numb.append(number)

		result.position = len(numb) + 1
			
		return result
