'''Lists all files in the current directory with an extension .py or a
    provided optional arguement 
        python filesOfType.py <extension>
'''

import os
import sys
import datetime
from prettytable import PrettyTable


def buildTable(directory,extension = ".py"):
'''Build a table of filenames and dates last modififed of files in  the directory with the specified extension'''
    table = PrettyTable(['Filename','Age'])
    #iterate through each file in the directory and check if it has the riht file extension
    for fname in directory:
        ext = os.path.splitext(fname)
        #If correct extension build a row and add it to the table
        if ext[1] == extension:
            fdate = os.path.getmtime(os.path.join(fpath,fname))
            date = datetime.datetime.fromtimestamp(fdate).strftime('%Y-%m-%d %H:%M:%S')
            table.add_row([fname,date])
    return table

#Current directory file path
fpath ="."
#Get all files in current directory
filesInDirectory = os.listdir(fpath)
#Check if an extension arguement was prvided
if len(sys.argv) > 1:
    ext = ''
    #Build extension string depending if a "." was included
    if sys.argv[1][0] == ".":
        ext = sys.argv[1]
    else:
        ext = "." + str(sys.argv[1])
    #Build table from directory and extension
    fileTable = buildTable(filesInDirectory,ext)
    print(fileTable)
else:
    print(buildTable(filesInDirectory))




# import sys
# sys.path.append('C:\\Users\\Michael\\AppData\\Roaming\\Python\\Python37\\Scripts')
