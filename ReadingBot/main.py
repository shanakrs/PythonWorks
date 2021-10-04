import pyttsx3
import PyPDF2

book = open('pyooo.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

page = pdfReader.getPage(7)
content = page.extractText()
print(content)


def reading_book(text):
    engine.say(text)
    engine.runAndWait()


reading_book(content)
