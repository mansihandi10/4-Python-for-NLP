# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:17:35 2024

@author: Hp
"""
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfReader
#Creating a pdf reader object
reader=PdfReader("matrix_basics.pdf")

print(len(reader.pages))

page=reader.pages[1]

text=page.extract_text()
print(text)

import re
sentence5="sharat twitted ,Wittnessing 68th republic day India from Rajpath , \new Delhi ,Mesmorizing performance by Indian Army !"
re.sub(r'([^\s\w]/_)+', ' ',sentence5).split()

"""
Extracting n-gram using custom function
"""
import re
def n_gram_extractor(input_str, n):
    tokens=re.sub(r'([^\s\w]/_)+', '', input_str).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])
        
n_gram_extractor("The Cute Little boy is playing with kitten", 2)
