# extracting_text.py
 
from PyPDF2 import PdfFileReader
from io import StringIO
from io import BytesIO

path = 'copy.pdf'
#path = 'LDA.pdf'

from tika import parser

raw = parser.from_file(path)
data = raw['content'].split('\n')
print(type(data))
for line in data:
    print(line)
    
