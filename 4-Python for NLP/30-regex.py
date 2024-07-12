# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 09:33:50 2024

@author: Hp
"""

import re
chat1 ="Hello, I am having an issue with my order # 412889912"
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern,chat1)
matches
#['412889912']

chat2="Hello, I am having an issue with my order 412889912"
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern,chat2)
matches
#['412889912']

chat3='My order 412889912 having an issue '
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern,chat3)
matches

def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
    
get_pattern_match('order[^\d]*(\d*)',chat1)
