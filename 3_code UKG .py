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
subjects=["Follows Instructions & does physical exercises (T1)","Jumps (T1)","Hops(T1)","Walks on a given line(T1)","Handles bat and ball (T2)","Tiptoes(T2)","Climbing Stairs (T3)","Balance on the Beam (T3)","Trace Straight Patterns(T1)","Curved Patterns (T2)","Handles a pair of scissors (T2)","Places object on a given outline (T1)","Thread Beads (T2)","Solves jigsaw puzzles (T2)","Buttons  The Shirt (T3)","T1_Has grip over crayon","T2_Has grip over crayon","T3_Has grip over crayon","Sort Objects by Shape /Colour (T3)","Colours within the given outline (T3)","Speaking Skills","EVS/Thinking Skills","Recognition of Letters","Counting of Numbers","INDIAN MUSIC","Content_Action","Listening & Participation","Friendly and Cheerful","Co-operates in Work & Play","No Of Days Present","No Of Working days","T2_Speaking Skills","T2_EVS/Thinking Skills","T2_Recognition of Letters","T2_Counting of Numbers","T2_INDIAN MUSIC","T2_Content_Action","T2_Listening & Participation","T2_Friendly and Cheerful","T2_Co-operates in Work & Play","T2_No Of Days Present","T2_No Of Working days","T3_Speaking Skills","T3_EVS/Thinking Skills","T3_Recognition of Letters","T3_Counting of Numbers","T3_INDIAN MUSIC","T3_Content_Action","T3_Listening & Participation","T3_Friendly and Cheerful","T3_Co-operates in Work & Play","T3_No Of Days Present","T3_No Of Working days","T1_Remarks","T2_Remarks","T3_Remarks"]

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
with open('3_UKG.html','r') as file:
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
        report[x] = record[x] if not (math.isnan(float(record[x]))) else ''

    report['terms'] = terms
    #report['exams'] = exams
    this_folder=os.path.dirname(os.path.abspath(__file__))
    html = html_template.format(**report)
    
    # Create a folder called `output` in the working directory for the next line to work 
    HTML(string = html,base_url=this_folder).write_pdf('./output/{}.pdf'.format(str(report['rollno']) +"_"+ report['student']), stylesheets=[css])






















#=================== 5. SAVE TO PDF  =========================================
