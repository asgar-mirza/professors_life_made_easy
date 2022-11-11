#author: Asgar Mehidi Mirza


#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import re
import datetime
import xlsxwriter

workbook = xlsxwriter.Workbook(r'C:\Users\faiza\Desktop\Faizaan\Spring 2020\TA\Assignment4.xlsx') 
worksheet = workbook.add_worksheet("My sheet")

worksheet.write('A1', 'Z-ID') 
worksheet.write('B1', 'Penalty for Submission')


row = 0
deadline = datetime.datetime.strptime("2020-02-13 00:00:00", "%Y-%m-%d %H:%M:%S")


for subdir, dirs, files in os.walk(r'C:\Users\faiza\Desktop\Faizaan\Spring 2020\TA\Assignment 4'):
    
    col = 0
    for filename in files:

        filepath = subdir + os.sep + filename

        
        if filepath.endswith("proj"):
            row += 1
            
            f = open(filepath, "r")
            firstLine = f.readline()
            
            penalty = 0
            zid = re.search(r'z\d{7}', firstLine)
            dateTime = re.search(r'([A-Z][a-z]{2})\s(\d{2})\s(2[0-3]|[01]?[0-9]):([0-5]?[0-9]):([0-5]?[0-9])\s(\d{4})',firstLine)
            
            s = dateTime.group(1)+" " + dateTime.group(2)+ " " + dateTime.group(6) + " " +dateTime.group(3)+":"+dateTime.group(4)+":"+dateTime.group(5)
            
            f = "%b %d %Y %H:%M:%S"
            x = datetime.datetime.strptime(s, f)
           
            worksheet.write(row, col, zid.group())
            

            if(x <= deadline):
                penalty = 0;
                
            elif(x > deadline and x <= deadline + datetime.timedelta(days=1)):
                penalty = -15
                
            elif( x > deadline + datetime.timedelta(days=1) and  x <= deadline + datetime.timedelta(days=2)):
                penalty = -30
                
            else:
                penalty = -100
            
            
            worksheet.write(row, col+1, penalty)
                     
workbook.close()
