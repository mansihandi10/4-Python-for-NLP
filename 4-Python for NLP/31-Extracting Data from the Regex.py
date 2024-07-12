# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 08:52:51 2024

@author: Hp
"""

import re
def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
    
chat1='You ask a lot of que 12345678912, abc@xyz.com'
chat2='Here it is:(123)-567-8912 a23@xy.com'
#to extracts the mail ID from the chat
get_pattern_match('[a-zA-Z0-9]*@[a-z]*\.[a-zA-Z0-9]*',chat1)
#'abc@xyz.com'
get_pattern_match('[a-zA-Z0-9]*@[a-z]*\.[a-zA-Z0-9]*',chat2)
#'a23@xy.com'

#to extract the mobile numbers from the chats

chat1='You ask a lot of que 12345678912, abc@xyz.com'
chat2='Here it is:(123)-567-8912 a23@xy.com'
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat1)
#('1234567891', '')
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat2)
#('', '(123)-567-8912')

#extract information from the wikipedia

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
get_pattern_match(r'age (\d+)',text)#'52'
get_pattern_match(r'Born(.*)\n', text).strip()
#'Elon Reeve Musk'

get_pattern_match(r'Born.*\n(.*)\(age', text).strip()
#'June 28, 1971'

get_pattern_match(r'age.*\n(.*)', text)
#'Pretoria, Transvaal, South Africa'