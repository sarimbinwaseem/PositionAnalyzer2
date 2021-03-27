import PyPDF2 
import os
import pickle

def importingFile(path):

	try:
		PDF_File = path
		pdfFileObj = open(PDF_File, 'rb') 
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
	except OSError:
		pass
		
	except FileNotFoundError:
		pass

	except:
		pass


	else:  
# printing number of pages in pdf file 
		pages  = int(pdfReader.numPages)
		totalpages = "Total number of pages in PDF:" + str(pages) 
		
		extracted_text = []

		with open("Result.pickle", "wb") as R_txt:
			for i in range(pages): 	
				# creating a page object 
				pageObj = pdfReader.getPage(i)  
				text = pageObj.extractText()
				extracted_text.append(text)
				
			pickle.dump(extracted_text, R_txt)	
			# print(extracted_text)
		pdfFileObj.close()

def check(obtMarksNum, totalNumbers):
		
	global alll
	try:	
		obt_number = obtMarksNum
		tot_number = totalNumbers
			
	except:
		pass
	else:
		
		
		noOfNumber = 0
		line = "1 ahead........"
		numb  = []
		# pickle_obj = []
		path = os.path.join(os.getcwd(), 'Result.pickle')
		file = open(path, "rb")
		pickle_obj = pickle.load(file)
		# print(pickle_obj) 
		results = []
		words = []
		for w in pickle_obj:
			words.append(w.split())
			# print(words)

		for number in range(obt_number + 1, tot_number):
			ToSearch1 = "(" +str(number) + ")"
			ToSearch2 = "(" +str(number) + "+" 
			ToSearch3 = "(" +str(number) + "^"
				
				
			for worde in words:
				# print(word)
				for word in worde:
					if word.find(ToSearch1) != -1 or word.find(ToSearch2) != -1 or word.find(ToSearch3) != -1:
						output = str(line) + " Scoring: "+ str(number) + " having " + str(round(((number/tot_number)*100),2)) + ' %.'
						# print(output)
						results.append(output)
						line = "1 more ahead..."
						noOfNumber += 1
						if number in numb:
							pass
						else:
							numb.append(number)
		# obtMarksNum = self.obtmarksedit.clear()
		position = len(numb) + 1
		# noOfNumber = students ahead
		file.close()
		alll = [results, position, noOfNumber]			
		return alll


		##################################################################################