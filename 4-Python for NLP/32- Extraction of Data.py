# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 09:10:59 2024

@author: Hp
"""
text='''
Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa
Canada
United States
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and Executive Chairman of X (formerly Twitter)
President of the Musk Foundation
Founder of The Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Partners	
Grimes (2018–2021)[1]
Children	11[a][3]
Parents	
Errol Musk
Maye Musk
Relatives	
Kimbal Musk (brother)
Tosca Musk (sister)
Lyndon Rive (cousin)
'''
import re
def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
    
def extract_personal_data(text):
    age=get_pattern_match(r'age (\d+)',text)
    Full_name=get_pattern_match(r'Born(.*)\n', text).strip()
  
    Birth_date=get_pattern_match(r'Born.*\n(.*)\(age', text).strip()
    Birth_place=get_pattern_match(r'age.*\n(.*)', text)
    return{
        'age':int(age),
        'name': Full_name.strip(),
        'birth_date': Birth_date.strip(),
        'birth_place': Birth_place.strip()}

extract_personal_data(text)

"""
{'age': 52,
 'name': 'Elon Reeve Musk',
 'birth_date': 'June 28, 1971',
 'birth_place': 'Pretoria, Transvaal, South Africa'}"""
    
#################################################    
    
text="""
Ambani in 2007
Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 67)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Occupation(s)	Chairman and MD, Reliance Industries
Spouse	Nita Ambani ​(m. 1985)​[3]
Children	3
Parents	
Dhirubhai Ambani (father)
Kokilaben Ambani (mother)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)

"""
extract_personal_data(text)
"""
{'age': 67,
 'name': 'Mukesh Dhirubhai Ambani',
 'birth_date': '19 April 1957',
 'birth_place': 'Aden, Colony of Aden'}"""

from PyPDF2 import PdfFileReader
from PyPDF2 import PdfReader

reader=PdfReader("kopargaon-part-1.pdf")
page=reader.pages[1]
print(len(reader.pages))

reader=PdfReader("matrix_basics.pdf")
#GETTING A SPECIFIC PAGE FROM THE PDF
page=reader.pages[2]
#printing the number of pages
print(len(reader.pages))