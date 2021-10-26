# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 09:36:33 2021

@author: Abid B
"""
from OdcesForms import SeleniumAbid
import datetime

def programSet(data, counter):
    select = SeleniumAbid.Select(SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_ddlDisaster"))
    date_str = str(data.iloc[counter]["DATE OF ENCOUNTER"])
    dateTime = datetime.date(date_str, '%m/%d/%Y')
    date = dateTime.date()
    print(date)
    changeDate = datetime.date(2021, 8, 1)
    print(changeDate)
    if (date < changeDate):    
        select.select_by_value('374')
    else:
        select.select_by_value('418')
def weeklyProg():
    select = SeleniumAbid.Select(SeleniumAbid.driver.find_element_by_id("ContentPlaceHolder1_ddlDisaster"))
    select.select_by_value('418')