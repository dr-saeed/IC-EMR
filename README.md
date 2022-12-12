# ImmunoCure Electronic Medical Record System - IC-EMR

## The code perform two major functions a) Makes folders of files and places them in their respective folders b) Takes a .csv file and creates a HTML with hyperlinks to the open the files in their folders

Of course the code can be used as a file organization tool, however, I've designed it for managing Medical Records of patients
##
All paper based records are first scanned using ClearScanner App
The files are stored according to medical record numbers (MRN) and pages are separated by - (minus sign) e.g. MR1234-pg2
The MRN are stored in a Patient Library (filename: IC_Pt_Lib.csv) containing (5 columns; 4th column is whether the patient is Active or not in the Clinic):
MRN, Patient Name, Contact number, Diagnosis
The Python code IC_EMR.py is placed in the same folder as all the scanned files
It checks to see if the folders already exist or not (then creates them)
It moves the files to their respective folders
If a file is already found in the folder the duplicate file is moved form the main folder to the 'Duplicate' folder
Finally, it makes the clickable hyperlinked HTML file for viewing the scanned documents according to the Patient Library file (.csv)
##
Dr. Mohammad Saeed
Consultant Rheumatology and Immunogenetics
ImmunoCure Center for Inflammatory Diseases
Email: msaeed@immunocure.pk
Twitter: DrMSaeed_pk, ImmunoCure_pk
