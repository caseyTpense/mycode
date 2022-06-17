import PyPDF2
import pyttsx3

#request input of pdf file
whichpdf= input('type the file name to be converted') 

#path of the requested PDF file
path = open(whichpdf, 'rb')

#creates pdfilereader object
pdfReader = PyPDF2.PdfFileReader(path)
#which page to start on
whichpage= int(input("which page number would you like to start on?"))

#sets the page number. subtract 1 for positional parameters
pagenum= pdfReader.getPage(int(whichpage - 1))  

#extract text from page
text= pagenum.extractText()


#reads the text

speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
