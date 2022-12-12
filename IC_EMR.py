from __future__ import print_function
import os
import shutil

log = open('IC_EMR_log.txt', 'w')

def EMR():

    global log

    # Obtain the path and prep list and dictionary
    path = os.getcwd()
    print (path, file=log)
    filelist = os.listdir(path)
    filedict = {}

    # Remove the program files from the list so that they are not placed in folders
    filelist.remove('IC_EMR.py')
    filelist.remove('IC_EMR_log.txt')
    filelist.remove('IC_Pt_Lib.csv')

    # Read list of files and make a dictionary for matching folder names
    for f in filelist:
        a = f.split('-')
        folder = a[0]
        filedict[folder] = [folder]

    # Make Duplicate Folder if it does not exist
    if not os.path.exists('Duplicate'):
            os.mkdir('Duplicate')

    # Make folders
    for fold in filedict:
        print (fold, file=log)
        
        if not os.path.exists(fold):
            os.mkdir(fold)
        else:
            print ('folder already exists', file=log)

    # Move files to respective folders
    for ff in filelist:
        aa = ff.split('-')
        direc = aa[0]
        new_path = os.path.join(path, direc, ff)

        if direc in filedict.keys():
            if not os.path.isfile(new_path):
                shutil.move(ff, os.path.join(path, direc)) 
                # print (ff, '\t', '\t', direc) # print results to screen

            else:
                print ('File exists in destination folder', ff, file=log)
                shutil.move(ff, os.path.join(path, 'Duplicate'))
        else:
            print ('Not present', ff, file=log)

    print ('End of EMR roytine', file = log)
    print ('', file = log)




def Lib():

    global log
    
    path = os.getcwd()
    print (path, file = log)

    pt_lib = open ("IC_Pt_Lib.csv", 'r')

    fdict = {}

    header = pt_lib.readline()

    for pt in pt_lib:
        pt = pt.rstrip()
        pt = pt.split(',')
        mrn = pt[0]
        name = pt[1]
        tel = pt[2]
        diag = pt[4]
        fdict[mrn] = name, tel, diag
        
    pt_lib.close()

    ## HTML

    fhtml = open ("IC_Pt_Lib.html", 'w')

    # Preparing HTML file headers

    print ('<table><align="center">', file=fhtml)
    print ('<TABLE BORDER="3" CELLSPACING="1" CELLPADDING="5">', file=fhtml)
    print ('<tr bgcolor="#006400"><td align="center" colspan="18"><B><H1><p style="color:#FFFFFF";>ImmunoCure Patient Library </B></H1><H4><I><p style="color:#FFFFFF";>Dr. Mohammad Saeed (www.immunocure.pk)</I></H4></td></tr>', file=fhtml)
    print ('<align="center">', file=fhtml)
    print ('<tr bgcolor="#9ACD32"><td>'+'Serial'+'</td><td>'+'MR #'+'</td><td>'+'Patient Name'+'</td><td>'+'Tel #'+'</td><td>'+'Diagnosis'+'</td></tr>', file = fhtml)


    # Printing the data to the HTML file as a Table

    serial = 1
    fhere = 0
    tot_rec = len(fdict.keys())
    link = ''
    col = "#FFF8DC"

    for mrno in sorted(fdict):

        pt_name = fdict[mrno][0]
        pt_tel = fdict[mrno][1]
        pt_diag = fdict[mrno][2]

        if os.path.isdir(mrno):
            lnk = os.path.join(mrno)
            link = '<a target="_blank" rel="noopener noreferrer" href='+str(lnk)+'>'+mrno+'</a>'
            fhere += 1
            col = "#9ACD32"
        else:
            link = mrno
            col = "#FFF8DC"
            

        # The next file prints actual data to html file.    
        print ('<tr bgcolor="#FFF8DC"><td>'+str(serial)+'</td><td align="center" bgcolor ='+col+'>'+link+'</td><td align="center">'+pt_name+'</td><td align="center">'+pt_tel+'</td><td align="center">'+pt_diag+'</td></tr>', file=fhtml)    
        
        serial += 1


    print ('</table>', file=fhtml)

    print ('<br>', file = fhtml)
    print ('<tr><td align="left">Patient Records Present: '+str(fhere)+'</td></tr>', file=fhtml)
    print ('<tr><td align="left">Total Library Records: '+str(tot_rec)+'</td></tr>', file=fhtml)

    print ('<br>', file = fhtml)
    print ('<br>', file = fhtml)
    print ('<table><align="center">', file=fhtml)


    fhtml.close()
    
    #raise SystemExit()

EMR()
Lib()
log.close()
