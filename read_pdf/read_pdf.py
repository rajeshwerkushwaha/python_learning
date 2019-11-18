# extracting_text.py
 
from PyPDF2 import PdfFileReader
from io import StringIO
from io import BytesIO

#path = 'copy.pdf'
path = 'LDA.pdf'

from tika import parser

raw = parser.from_file(path)
data = raw['content'].split('\n')
print(type(data))
for line in data:
    print(line)
    


# def getPDFContent(path):
#     content = ""
#     num_pages = 1
#     p = open(path, "rb")
#     pdf = PdfFileReader(p)
#     for i in range(0, num_pages):
#         print(pdf.getPage(i).extractText())
#         content += pdf.getPage(i).extractText() + "\n"
#     content = " ".join(content.replace(u"\xa0", " ").strip().split())
#     return content

# def text_extractor(path):
# 	with open(path, 'rb') as f:
# 		pdf = PdfFileReader(f)
# 		# get the first page
# 		page = pdf.getPage(1)
# 		print(page)
# 		print('Page type: {}'.format(str(type(page))))
# 		text = page.extractText()
# 		print(text)

# if __name__ == '__main__':
    
# 	#pdfContent = StringIO(getPDFContent(path).encode("ascii", "ignore").decode('utf-8'))
#     pdfContent = BytesIO(getPDFContent(path).decode('utf-8'))
#     for line in pdfContent:
#         print(line.strip())

# pdfFileObj = open(path,'rb')     #'rb' for read binary mode
# pdfReader = PdfFileReader(pdfFileObj)
# print(pdfReader.numPages)
# pageObj = pdfReader.getPage(0)          #'9' is the page number
# pages_text = pageObj.extractText()
# #print(pageObj.extractText().decode('utf-8'))

# for line in pages_text.split('\n'):
# 	print(line)

# import slate3k as slate

# with open(path,'rb') as f:
#     extracted_text = slate.PDF(f)
# print(extracted_text)