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
from weasyprint import HTML,CSS
import math
from helpers import get_grade_letter, calculate_gpa, total_gpa
from tkinter import filedialog

#===================== 1. LOAD DATA ==========================================
# GTK_FOLDER = r'C:\Users\seu5cob\AppData\Local\Programs\Python\Python310\GTK\gtk-nsis-pack\bin'
# os.environ['PATH'] = GTK_FOLDER + os.pathsep + os.environ.get('PATH', '')
#data_file = Path('./data/records-edit.csv')
data_file = filedialog.askopenfilename()
df = pd.read_csv(data_file)

#suganthi : Defined values
exams = ['MT1','MT2','MT3']
terms = ['Term1','Term2','Term3']


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
    report['exam'] = record['EXAM']
    report['mt1_eng_score'] = record['MT1_ENG']
    report['mt1_math_score'] = record['MT1_MATH'] if not (math.isnan(record['MT1_MATH'])) else (record['MT1_ENT'] if not (math.isnan(record['MT1_ENT'])) else '')
    report['mt1_ent_score'] = record['MT1_ENT']
    report['mt1_phy_score'] = record['MT1_PHY']
    report['mt1_che_score'] = record['MT1_CHE']
    report['mt1_bio_score'] = record['MT1_BIO']
    report['mt1_total'] = record['MT1_TOTAL']

    report['mt2_eng_score'] = record['MT2_ENG']
    report['mt2_math_score'] = record['MT2_MATH'] if not (math.isnan(record['MT2_MATH'])) else (
        record['MT2_ENT'] if not (math.isnan(record['MT2_ENT'])) else '')
    report['mt2_ent_score'] = record['MT2_ENT']
    report['mt2_phy_score'] = record['MT2_PHY']
    report['mt2_che_score'] = record['MT2_CHE']
    report['mt2_bio_score'] = record['MT2_BIO']
    report['mt2_total'] = record['MT2_TOTAL']

    report['mt3_eng_score'] = record['MT3_ENG']
    report['mt3_math_score'] = record['MT3_MATH'] if not (math.isnan(record['MT3_MATH'])) else (
        record['MT3_ENT'] if not (math.isnan(record['MT3_ENT'])) else '')
    report['mt3_ent_score'] = record['MT3_ENT']
    report['mt3_phy_score'] = record['MT3_PHY']
    report['mt3_che_score'] = record['MT3_CHE']
    report['mt3_bio_score'] = record['MT3_BIO']
    report['mt3_total'] = record['MT3_TOTAL']

    report['term1_remarks'] = record['TERM1_REMARKS'] if not (record['TERM1_REMARKS']) else 'Good luck!'
    report['term2_remarks'] = record['TERM2_REMARKS'] if not (record['TERM2_REMARKS']) else 'Good luck!'
    report['term3_remarks'] = record['TERM3_REMARKS'] if not (record['TERM3_REMARKS']) else 'Good luck!'
    report['terms'] = terms
    report['exams'] = exams
    html = html_template.format(**report)
    
    # Create a folder called `output` in the working directory for the next line to work 
    HTML(string = html).write_pdf('./output/{}.pdf'.format(report['student']), stylesheets=[css])






















#=================== 5. SAVE TO PDF  =========================================
