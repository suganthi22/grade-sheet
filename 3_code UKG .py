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
subjects=["T1_Attentiveness","T2_Attentiveness","T3_Attentiveness","T1_Comprehension","T2_Comprehension","T3_Comprehension","T1_Clarity in Speech","T2_Clarity in Speech","T3_Clarity in Speech","T1_Structure/Vocabulary","T2_Structure/Vocabulary","T3_Structure/Vocabulary","T1_Fluency","T2_Fluency","T3_Fluency","T1_Expression of Ideas","T2_Expression of Ideas","T3_Expression of Ideas","T1_Conversation","T2_Conversation","T3_Conversation","T1_Content","T2_Content","T3_Content","T1_Expression","T2_Expression","T3_Expression","T1_Pronunciation &Intonation","T2_Pronunciation &Intonation","T3_Pronunciation &Intonation","T1_Expression / Fluency","T2_Expression / Fluency","T3_Expression / Fluency","T1_Sequence","T2_Sequence","T3_Sequence","T1_Recognition of words","T2_Recognition of words","T3_Recognition of words","T1_Pronunciation & Expression","T2_Pronunciation & Expression","T3_Pronunciation & Expression","T1_Comprehension","T2_Comprehension","T3_Comprehension","T1_Fluency","T2_Fluency","T3_Fluency","T1_Neatness","T2_Neatness","T3_Neatness","T1_Legibility","T2_Legibility","T3_Legibility","T1_Spacing","T2_Spacing","T3_Spacing","T1_Spelling Skills /Word Building","T2_Spelling Skills /Word Building","T3_Spelling Skills /Word Building","T1_Composition & Structure","T2_Composition & Structure","T3_Composition & Structure","T1_Vocabulary","T2_Vocabulary","T3_Vocabulary","T1_Eng. Literature","T2_Eng. Literature","T3_Eng. Literature","T1_Eng. Language","T2_Eng. Language","T3_Eng. Language","T1_Attentiveness","T2_Attentiveness","T3_Attentiveness","T1_Class Participation","T2_Class Participation","T3_Class Participation","T1_Comprehension","T2_Comprehension","T3_Comprehension","T1_Recitatio","T2_Recitatio","T3_Recitatio","T1_Reading","T2_Reading","T3_Reading","T1_Formation of Letters /Words","T2_Formation of Letters /Words","T3_Formation of Letters /Words","T1_Class Assignments","T2_Class Assignments","T3_Class Assignments","T1_Number Recognition","T2_Number Recognition","T3_Number Recognition","T1_Conceptual Skillls","T2_Conceptual Skillls","T3_Conceptual Skillls","T1_Accuracy in Basic Operations","T2_Accuracy in Basic Operations","T3_Accuracy in Basic Operations","T1_Ability to Solve Problems","T2_Ability to Solve Problems","T3_Ability to Solve Problems","T1_Ability for Mental Calculation","T2_Ability for Mental Calculation","T3_Ability for Mental Calculation","T1_Class Assignments","T2_Class Assignments","T3_Class Assignments","T1_Class Participation","T2_Class Participation","T3_Class Participation","T1_Comprehension & Interpretation of Information","T2_Comprehension & Interpretation of Information","T3_Comprehension & Interpretation of Information","T1_Class Assignments","T2_Class Assignments","T3_Class Assignments","T1_Compulsory Tamil/ Hindi","T2_Compulsory Tamil/ Hindi","T3_Compulsory Tamil/ Hindi","T1_Thinking Skills","T2_Thinking Skills","T3_Thinking Skills","T1_Art/Craft","T2_Art/Craft","T3_Art/Craft","T1_Indian Music & Sloka","T2_Indian Music & Sloka","T3_Indian Music & Sloka","T1_Western Music","T2_Western Music","T3_Western Music","T1_Dance","T2_Dance","T3_Dance","T1_Yoga","T2_Yoga","T3_Yoga","T1_Physical Education","T2_Physical Education","T3_Physical Education","T1_Retention & Recall","T2_Retention & Recall","T3_Retention & Recall","T1_Has the Right Attitude","T2_Has the Right Attitude","T3_Has the Right Attitude","T1_Works lndependently","T2_Works lndependently","T3_Works lndependently","T1_Follows Directions","T2_Follows Directions","T3_Follows Directions","T1_Completes Assignments on Time","T2_Completes Assignments on Time","T3_Completes Assignments on Time","T1_Submits Neat Work","T2_Submits Neat Work","T3_Submits Neat Work","T1_Brings Books Regularly","T2_Brings Books Regularly","T3_Brings Books Regularly","T1_Actively Participates in Class Activities","T2_Actively Participates in Class Activities","T3_Actively Participates in Class Activities","T1_ls Attentive in Class","T2_ls Attentive in Class","T3_ls Attentive in Class","T1_Works Well In a Group","T2_Works Well In a Group","T3_Works Well In a Group","T1_ls Polite and Courteous","T2_ls Polite and Courteous","T3_ls Polite and Courteous","T1_Respects Other’s Property","T2_Respects Other’s Property","T3_Respects Other’s Property","T1_Is Punctual","T2_Is Punctual","T3_Is Punctual","T1_Co-operates with Teachers and Students","T2_Co-operates with Teachers and Students","T3_Co-operates with Teachers and Students","T1_Behaves Well Inside and Outside Class","T2_Behaves Well Inside and Outside Class","T3_Behaves Well Inside and Outside Class","T1_Accepts Responsibilities","T2_Accepts Responsibilities","T3_Accepts Responsibilities","T1_Helps Others","T2_Helps Others","T3_Helps Others","T1_Observes School and Class Rules","T2_Observes School and Class Rules","T3_Observes School and Class Rules","T1_Neatly Dressed & in Proper Uniform","T2_Neatly Dressed & in Proper Uniform","T3_Neatly Dressed & in Proper Uniform","T1_ATTENDANCE","T2_ATTENDANCE","T3_ATTENDANCE"]
subject_names =["Attentiveness","Comprehension","Clarity in Speech","Structure/Vocabulary","Fluency","Expression of Ideas","Conversation","Content","Expression","Pronunciation &Intonation","Expression / Fluency","Sequence","Recognition of words","Pronunciation & Expression","Comprehension","Fluency","Neatness","Legibility","Spacing","Spelling Skills /Word Building","Composition & Structure","Vocabulary","Eng. Literature","Eng. Language","Attentiveness","Class Participation","Comprehension","Recitatio","Reading","Formation of Letters /Words","Class Assignments","Number Recognition","Conceptual Skillls","Accuracy in Basic Operations","Ability to Solve Problems","Ability for Mental Calculation","Class Assignments","Class Participation","Comprehension & Interpretation of Information","Class Assignments","Compulsory Tamil/ Hindi","Thinking Skills","Art/Craft","Indian Music & Sloka","Western Music","Dance","Yoga","Physical Education","Retention & Recall","Has the Right Attitude","Works lndependently","Follows Directions","Completes Assignments on Time","Submits Neat Work","Brings Books Regularly","Actively Participates in Class Activities","ls Attentive in Class","Works Well In a Group","ls Polite and Courteous","Respects Other’s Property","Is Punctual","Co-operates with Teachers and Students","Behaves Well Inside and Outside Class","Accepts Responsibilities","Helps Others","Observes School and Class Rules","Neatly Dressed & in Proper Uniform","ATTENDANCE"]
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
with open('4_Std1_2.html','r') as file:
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
    report['subjects'] = subjects
    report['subject_names'] = subject_names
    #report['subject_id'] = {}
    report['marks'] = []
   # report['exam'] = record['EXAM']
    
    for x in subjects:
       #report['subject_id'][x] = int(record[x] if not (math.isnan(float(record[x]))) else 0)
        report['marks'].append(int(record[x] if not (math.isnan(float(record[x]))) else 0))
    #[x] = record[x]
    report['terms'] = terms
    print(report)
    #report['exams'] = exams
    this_folder=os.path.dirname(os.path.abspath(__file__))
    html = html_template.format(**report)
    
    # Create a folder called `output` in the working directory for the next line to work 
    HTML(string = html,base_url=this_folder).write_pdf('./output/{}.pdf'.format(str(report['rollno']) +"_"+ report['student']), stylesheets=[css])






















#=================== 5. SAVE TO PDF  =========================================
