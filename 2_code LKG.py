"""
Generate pdf reports in bulk using a single csv file

TO DO
======
We are going generate a PDF report for each record in the CSV file using a 
predefined HTML template

    0. Data generation [Optional]
    1. Load and inspect data
    2. Preprocessing - generate grade letters
    3. Quick review python string formatting
    4. A simple template using Python string formatting
     - [Optional] Use Jinja2 template engine
    4. Generate pdf using weasyprint

"""
#===================== IMPORTS ===============================================
import os
from pathlib import Path
import numpy as np
import pandas as pd
from ctypes.util import find_library

find_library('gobject-2.0')
from weasyprint import HTML,CSS

import math
from helpers import get_grade_letter, calculate_gpa, total_gpa
from tkinter import filedialog
# Importing Tkinter module
from tkinter import *
# from tkinter.ttk import *
 
'''# Creating master Tkinter window
master = Tk()
master.geometry("175x175")
 
# Tkinter string variable
# able to store any string value
v = StringVar(master, "1")
 
# Dictionary to create multiple buttons
values = {"RadioButton 1" : "1",
          "RadioButton 2" : "2",
          "RadioButton 3" : "3",
          "RadioButton 4" : "4",
          "RadioButton 5" : "5"}
 
# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
    Radiobutton(master, text = text, variable = v,
                value = value, indicator = 0,
                background = "light blue").pack(fill = X, ipady = 5)
 
# Infinite loop can be terminated by
# keyboard or mouse interrupt
# or by any predefined function (destroy())
mainloop()'''
#===================== 1. LOAD DATA ==========================================
# GTK_FOLDER = r'C:\Users\seu5cob\AppData\Local\Programs\Python\Python310\GTK\gtk-nsis-pack\bin'
# os.environ['PATH'] = GTK_FOLDER + os.pathsep + os.environ.get('PATH', '')
#data_file = Path('./data/records-edit.csv')
data_file = filedialog.askopenfilename()
df = pd.read_csv(data_file)

#suganthi : Defined values
#exams = ['MIDYEAR EXAM','PT','IA','TOTAL','GRADE','ANNUAL','PT','IA','TOTAL','GRADE']
terms = ['Term I','Term II','TERM III']
subjects=["T1_Attentiveness","T1_Comprehension","T1_Clarity","T1_General conversation","T1_Recitation","T1_Narration","T1_Phonetic sound","T1_Recognition of Letters","T1_Formation of Patterns","T1_Formation of Letters","T1_Class Assignment","T1_Recognition of Numbers","T1_Formation of Numbers","T1_Concept Counting","T1_Class Assignment","T1_Class participation","T1_Class Assignment","T1_DRAWING / COLOURING","T1_INDIAN MUSIC","T1_SOCIAL SKILLS","T1_No of Days Present","T1_No of Working days","T2_Attentiveness","T2_Comprehension","T2_Clarity","T2_General conversation","T2_Recitation","T2_Narration","T2_Phonetic sound","T2_Recognition of Letters","T2_Formation of Patterns","T2_Formation of Letters","T2_Class Assignment","T2_Recognition of Numbers","T2_Formation of Numbers","T2_Concept Counting","T2_Class Assignment","T2_Class participation","T2_Class Assignment","T2_DRAWING / COLOURING","T2_INDIAN MUSIC","T2_SOCIAL SKILLS","T2_No of Days Present","T2_No of Working days","T3_Attentiveness","T3_Comprehension","T3_Clarity","T3_General conversation","T3_Recitation","T3_Narration","T3_Phonetic sound","T3_Recognition of Letters","T3_Formation of Patterns","T3_Formation of Letters","T3_Class Assignment","T3_Recognition of Numbers","T3_Formation of Numbers","T3_Concept Counting","T3_Class Assignment","T3_Class participation","T3_Class Assignment","T3_DRAWING / COLOURING","T3_INDIAN MUSIC","T3_SOCIAL SKILLS","T3_No of Days Present","T3_No of Working days","T1_Remarks","T2_Remarks","T3_Remarks"]
#===================== 2. PROCESS DATA =======================================
records = df.to_dict(orient = 'records')
record = records[0]

report = {}
#ENG	MATH	ENT	PHY	CHE	BIO

# report['student'] = record['STUDENT NAME']
# report['section'] = record['SECTION']
# report['rollno'] = record['ROLL NO']
# report['usn'] = record['USN NO']
# report['exam'] = record['EXAM']
# report['eng_score'] = record['ENG']
# report['math_score'] = record['MATH'] if not (math.isnan(record['MATH'])) else (record['ENT'] if not (math.isnan(record['ENT'])) else 0)
# report['ent_score'] = record['ENT']
# report['phy_score'] = record['PHY']
# report['che_score'] = record['CHE']
# report['bio_score'] = record['BIO']
# report['total'] = record['TOTAL']
# report['remarks'] = record['REMARKS'] if not (math.isnan(record['REMARKS'])) else 'Good luck!'
# report['math_grade'] = get_grade_letter(record['math'])
# report['math_gpa'] = calculate_gpa(record['math'])
#
# report['physics_score'] = record['physics']
# report['physics_grade'] = get_grade_letter(record['physics'])
# report['physics_gpa'] = calculate_gpa(record['physics'])
#
# report['chemistry_score'] = record['chemistry']
# report['chemistry_grade'] = get_grade_letter(record['chemistry'])
# report['chemistry_gpa'] = calculate_gpa(record['chemistry'])

#report['total_gpa'] = total_gpa(record['math'],
                                # record['physics'],
                                # record['chemistry']
    
    # )

#=================== 3. A SIMPLE TEMPLATE ====================================

# template = """
# ==================== REPORT CARD ======================
# Subject |        Score      | Grade      | GPA
# -------------------------------------------------------
#                     {student}
# Math        {math_score:^7} {math_grade:^7} {math_gpa:^7}
# Physics     {physics_score:^7} {physics_grade:^7} {physics_gpa:^7}
# Chemistry   {chemistry_score:^7} {chemistry_grade:^7} {chemistry_gpa:^7}
# Total GPA   {total_gpa}
#
#
# """
#
# output = template.format(**report)



#=================== 4. A BETTER TEMPLATE USING WEASYPRINT  ==================
with open('2_LKG.html','r') as file:
    html_template = file.read()
    
css = CSS('bootstrap-5.1.3-dist/css/bootstrap.min.css')


records = df.to_dict(orient = 'records')

for record in records:

    report = {}
    
    # report['student'] = record['name']
    # report['math_score'] = record['math']
    # report['math_grade'] = get_grade_letter(record['math'])
    # report['math_gpa'] = calculate_gpa(record['math'])
    #
    # report['physics_score'] = record['physics']
    # report['physics_grade'] = get_grade_letter(record['physics'])
    # report['physics_gpa'] = calculate_gpa(record['physics'])
    #
    # report['chemistry_score'] = record['chemistry']
    # report['chemistry_grade'] = get_grade_letter(record['chemistry'])
    # report['chemistry_gpa'] = calculate_gpa(record['chemistry'])
    #
    # report['total_gpa'] = total_gpa(record['math'],
    #                                 record['physics'],
    #                                 record['chemistry']
        
        # )
    report['student'] = record['STUDENT NAME']
    report['section'] = record['SECTION']
    report['rollno'] = record['ROLL NO']
    report['usn'] = record['USN NO']
   # report['exam'] = record['EXAM']
    
    for x in subjects:
        print(x)
        print(record[x])
        report[x] = record[x] if not (math.isnan(float(record[x]))) else ''

    report['terms'] = terms
    #report['exams'] = exams
    this_folder=os.path.dirname(os.path.abspath(__file__))
    html = html_template.format(**report)
    
    # Create a folder called `output` in the working directory for the next line to work 
    HTML(string = html,base_url=this_folder).write_pdf('./output/{}.pdf'.format(str(report['rollno']) +"_"+ report['student']), stylesheets=[css])






















#=================== 5. SAVE TO PDF  =========================================
