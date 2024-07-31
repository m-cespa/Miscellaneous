# pdf_merger.py
# tool using PyPDF2 to merge select all pages (except potentially cover sheets) from directory containing pdfs

import PyPDF2, os

# get list of all file names
pdfFiles = []
dir = input('Enter directory path: ')
os.chdir(dir)
for file_name in os.listdir():
    if file_name.endswith('.pdf'):
        pdfFiles.append(file_name)

pdfFiles.sort(key=str.lower)

PdfWriter = PyPDF2.PdfWriter()

for file_name in pdfFiles:
    pdfReader = PyPDF2.PdfReader(open(file_name, 'rb'))
    for pageNum in range(1, len(pdfReader.pages)):
        pageObj = pdfReader.pages[pageNum]
        PdfWriter.add_page(pageObj)

pdfOutput = open('merged.pdf', 'wb')
PdfWriter.write(pdfOutput)
pdfOutput.close()