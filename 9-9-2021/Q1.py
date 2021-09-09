# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 19:26:22 2021

@author: Admin
"""

from datetime import date

today = date.today()
#print("Today's date:", today)
number_of_days=int(input("Enter a number of days: "))
def get_date(number_of_days):
    
    if(number_of_days%2==0):
        print(today,'+',number_of_days)
    else:
        print(today,'-',number_of_days)
get_date(number_of_days);
