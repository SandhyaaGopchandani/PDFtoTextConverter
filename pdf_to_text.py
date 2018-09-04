from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams
import io
import os

#parse pdf file into text
def pdfparser(filename):
    manager = PDFResourceManager()
    output = io.BytesIO()
    codec = 'utf-8'
    laparams = LAParams()

    converter = TextConverter(manager, output, codec=codec, laparams=laparams)

    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(manager, converter)

    #pdf_file = open(file, 'rb')
    pdf_file = open(filename, 'rb')

    # Process each page contained in the document.
    for page in PDFPage.get_pages(pdf_file):
        interpreter.process_page(page)
    pdf_file.close()
    converter.close()
    text = output.getvalue()

    return text

#write text to a text file
def write_to_text_file(filename, data, directory):
    path = " "
    os.chdir(path)
    if not os.path.isdir(directory):
        os.makedirs(directory)
    filename = filename + '.txt'

    # print(filename)
    filepath = os.path.join(path + directory, filename)
    # print(filepath)

    file = open(filepath, 'w+')
    file.write(data)
    file.close()


#iterate through directory to convert many pdf files and convert to text files
folder_from = "folder you have pdf files in"
for file in os.listdir(folder_from):
    if file != '.DS_Store':
        filename = file.split('.')[0]
        print(filename)
        filepath = os.path.join(folder_from, file)
        data = pdfparser(filepath)
        write_to_text_file(filename, data, 'textfile-name.txt')