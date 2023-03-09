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
exams = ['UT1','MT1','QTLY','MT2','HY','UT2','ANNUAL']
terms = ['Ist Term','2nd Term','3rd Term']


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
with open('template2.html','r') as file:
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
   
    report['UT1_eng_score'] = record['UT1_ENG'] if not (math.isnan(record['UT1_ENG'])) else ''
    report['UT1_math_ent_am_score'] = record['UT1_MATH'] if not (math.isnan(record['UT1_MATH'])) else (record['UT1_ENT'] if not (math.isnan(record['UT1_ENT'])) else (record['UT1_AM']))
    report['UT1_phy_acc_score'] = record['UT1_PHY'] if not (math.isnan(record['UT1_PHY'])) else (record['UT1_ACC'] if not (math.isnan(record['UT1_ACC'])) else '')
    report['UT1_che_bst_score'] = record['UT1_CHE'] if not (math.isnan(record['UT1_CHE'])) else (record['UT1_BST'] if not (math.isnan(record['UT1_BST'])) else '')
    report['UT1_bio_csc_eco_score'] = record['UT1_BIO'] if not (math.isnan(record['UT1_BIO'])) else (record['UT1_CSC'] if not (math.isnan(record['UT1_CSC'])) else (record['UT1_ECO']))
    report['UT1_total'] = record['UT1_TOTAL'] if not (math.isnan(record['UT1_TOTAL'])) else ''


    report['MT1_eng_score'] = record['MT1_ENG'] if not (math.isnan(record['MT1_ENG'])) else ''
    report['MT1_math_ent_am_score'] = record['MT1_MATH'] if not (math.isnan(record['MT1_MATH'])) else (record['MT1_ENT'] if not (math.isnan(record['MT1_ENT'])) else (record['MT1_AM']))
    report['MT1_phy_acc_score'] = record['MT1_PHY'] if not (math.isnan(record['MT1_PHY'])) else (record['MT1_ACC'] if not (math.isnan(record['MT1_ACC'])) else '')
    report['MT1_che_bst_score'] = record['MT1_CHE'] if not (math.isnan(record['MT1_CHE'])) else (record['MT1_BST'] if not (math.isnan(record['MT1_BST'])) else '')
    report['MT1_bio_csc_eco_score'] = record['MT1_BIO'] if not (math.isnan(record['MT1_BIO'])) else (record['MT1_CSC'] if not (math.isnan(record['MT1_CSC'])) else (record['MT1_ECO']))
    report['MT1_total'] = record['MT1_TOTAL'] if not (math.isnan(record['MT1_TOTAL'])) else ''

    
    report['QLY_eng_score'] = record['QLY_ENG'] if not (math.isnan(record['QLY_ENG'])) else ''
    report['QLY_math_ent_am_score'] = record['QLY_MATH'] if not (math.isnan(record['QLY_MATH'])) else (record['QLY_ENT'] if not (math.isnan(record['QLY_ENT'])) else (record['QLY_AM']))
    report['QLY_phy_acc_score'] = record['QLY_PHY'] if not (math.isnan(record['QLY_PHY'])) else (record['QLY_ACC'] if not (math.isnan(record['QLY_ACC'])) else '')
    report['QLY_che_bst_score'] = record['QLY_CHE'] if not (math.isnan(record['QLY_CHE'])) else (record['QLY_BST'] if not (math.isnan(record['QLY_BST'])) else '')
    report['QLY_bio_csc_eco_score'] = record['QLY_BIO'] if not (math.isnan(record['QLY_BIO'])) else (record['QLY_CSC'] if not (math.isnan(record['QLY_CSC'])) else (record['QLY_ECO']))
    report['QLY_total'] = record['QLY_TOTAL'] if not (math.isnan(record['QLY_TOTAL'])) else ''

    report['MT2_eng_score'] = record['MT2_ENG'] if not (math.isnan(record['MT2_ENG'])) else ''
    report['MT2_math_ent_am_score'] = record['MT2_MATH'] if not (math.isnan(record['MT2_MATH'])) else (record['MT2_ENT'] if not (math.isnan(record['MT2_ENT'])) else (record['MT2_AM']))
    report['MT2_phy_acc_score'] = record['MT2_PHY'] if not (math.isnan(record['MT2_PHY'])) else (record['MT2_ACC'] if not (math.isnan(record['MT2_ACC'])) else '')
    report['MT2_che_bst_score'] = record['MT2_CHE'] if not (math.isnan(record['MT2_CHE'])) else (record['MT2_BST'] if not (math.isnan(record['MT2_BST'])) else '')
    report['MT2_bio_csc_eco_score'] = record['MT2_BIO'] if not (math.isnan(record['MT2_BIO'])) else (record['MT2_CSC'] if not (math.isnan(record['MT2_CSC'])) else (record['MT2_ECO']))
    report['MT2_total'] = record['MT2_TOTAL'] if not (math.isnan(record['MT2_TOTAL'])) else ''
    
    report['HLY_eng_score'] = record['HLY_ENG'] if not (math.isnan(record['HLY_ENG'])) else ''
    report['HLY_math_ent_am_score'] = record['HLY_MATH'] if not (math.isnan(record['HLY_MATH'])) else (record['HLY_ENT'] if not (math.isnan(record['HLY_ENT'])) else (record['HLY_AM']))
    report['HLY_phy_acc_score'] = record['HLY_PHY'] if not (math.isnan(record['HLY_PHY'])) else (record['HLY_ACC'] if not (math.isnan(record['HLY_ACC'])) else '')
    report['HLY_che_bst_score'] = record['HLY_CHE'] if not (math.isnan(record['HLY_CHE'])) else (record['HLY_BST'] if not (math.isnan(record['HLY_BST'])) else '')
    report['HLY_bio_csc_eco_score'] = record['HLY_BIO'] if not (math.isnan(record['HLY_BIO'])) else (record['HLY_CSC'] if not (math.isnan(record['HLY_CSC'])) else (record['HLY_ECO']))
    report['HLY_total'] = record['HLY_TOTAL'] if not (math.isnan(record['HLY_TOTAL'])) else ''


    report['UT2_eng_score'] = record['UT2_ENG'] if not (math.isnan(record['UT2_ENG'])) else ''
    report['UT2_math_ent_am_score'] = record['UT2_MATH'] if not (math.isnan(record['UT2_MATH'])) else (record['UT2_ENT'] if not (math.isnan(record['UT2_ENT'])) else (record['UT2_AM']))
    report['UT2_phy_acc_score'] = record['UT2_PHY'] if not (math.isnan(record['UT2_PHY'])) else (record['UT2_ACC'] if not (math.isnan(record['UT2_ACC'])) else '')
    report['UT2_che_bst_score'] = record['UT2_CHE'] if not (math.isnan(record['UT2_CHE'])) else (record['UT2_BST'] if not (math.isnan(record['UT2_BST'])) else '')
    report['UT2_bio_csc_eco_score'] = record['UT2_BIO'] if not (math.isnan(record['UT2_BIO'])) else (record['UT2_CSC'] if not (math.isnan(record['UT2_CSC'])) else (record['UT2_ECO']))
    report['UT2_total'] = record['UT2_TOTAL'] if not (math.isnan(record['UT2_TOTAL'])) else ''


    report['ANN_eng_score'] = record['ANN_ENG'] if not (math.isnan(record['ANN_ENG'])) else ''
    report['ANN_math_ent_am_score'] = record['ANN_MATH'] if not (math.isnan(record['ANN_MATH'])) else (record['ANN_ENT'] if not (math.isnan(record['ANN_ENT'])) else (record['ANN_AM']))
    report['ANN_phy_acc_score'] = record['ANN_PHY'] if not (math.isnan(record['ANN_PHY'])) else (record['ANN_ACC'] if not (math.isnan(record['ANN_ACC'])) else '')
    report['ANN_che_bst_score'] = record['ANN_CHE'] if not (math.isnan(record['ANN_CHE'])) else (record['ANN_BST'] if not (math.isnan(record['ANN_BST'])) else '')
    report['ANN_bio_csc_eco_score'] = record['ANN_BIO'] if not (math.isnan(record['ANN_BIO'])) else (record['ANN_CSC'] if not (math.isnan(record['ANN_CSC'])) else (record['ANN_ECO']))
    report['ANN_total'] = record['ANN_TOTAL'] if not (math.isnan(record['ANN_TOTAL'])) else ''


    report['term1_remarks'] = record['TERM1_REMARKS'] if not (record['TERM1_REMARKS']) else 'Good luck!'
    report['term2_remarks'] = record['TERM2_REMARKS'] if not (record['TERM2_REMARKS']) else 'Good luck!'
    report['term3_remarks'] = record['TERM3_REMARKS'] if not (record['TERM3_REMARKS']) else 'Good luck!'
    report['terms'] = terms
    report['exams'] = exams
    html = html_template.format(**report)
    
    # Create a folder called `output` in the working directory for the next line to work 
    HTML(string = html).write_pdf('./output/{}.pdf'.format(report['student']), stylesheets=[css])






















#=================== 5. SAVE TO PDF  =========================================
