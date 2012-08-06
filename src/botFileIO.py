from __future__ import print_function

'''Created on 05/08/2012'''
'''Last Modified on 06/08/2012'''
'''Version 0.1.3'''
'''@author: Rebecca Miyamoto'''

from datetime import datetime, timedelta
import string, fileinput

'''Method for reading a line out of a datafile, using the lineIdent (the first word on the line)'''

def readTime(filename, lineIdent):
    
    timeToReturn = "null"
    
    with open(filename, 'r') as dataFile:
        for line in dataFile:
            lineScan=string.rstrip(line)
            lineScan=string.split(lineScan)
            if (lineScan[0] == lineIdent):
                timeToReturn = datetime.strptime(lineScan[2], '%d/%m/%Y/%H:%M:%S')
    
    return timeToReturn

def readLine(filename, lineIdent):
    
    lineToReturn = ""
    
    with open(filename, 'r') as dataFile:
        for line in dataFile:
            lineScan=string.rstrip(line)
            lineScan=string.split(lineScan)
            if (lineScan[0] == lineIdent):
                lineToReturn = lineScan
            
    return lineToReturn

'''For appending a line to a data file'''
def createLine(filename, line):
    dataFile = open(filename, 'a')
    dataFile.write("\n" + line)
    dataFile.close()

def getLineCount(filename):
    num_lines = 0
    with open(filename, 'r') as dataFile:
        for line in dataFile:
            num_lines += 1
    return num_lines

def getCurrentDateTime():
    return datetime.now()

def isThreeHour(dateTimeOne, dateTimeTwo):
    
    threeHours = timedelta(hours=3)
    
    if (dateTimeTwo - dateTimeOne >= threeHours):
        isThreeHour = 1
    else:
        isThreeHour = 0
    
    return isThreeHour

def timeLeft(dateTimeOne, dateTimeTwo):
    return int(10800 - (dateTimeTwo - dateTimeOne).total_seconds())

'''For editing or creating a line in a file'''
def editLine(filename, username, increment):
    
    setFlag = 0
    
    lineCount = getLineCount(filename)
    print(lineCount, end='')
    
    dataFile = open(filename, 'r')
    for line in dataFile:
        lineScan=string.rstrip(line)
        lineScan=string.split(lineScan)
        if (lineScan[0] == username):
            setFlag = 1
    dataFile.close()
    
    if (setFlag == 1):
        '''Search for the line in question'''
        for line in fileinput.input("witch",inplace=1):
            
            '''Format the line so the whole username is line[0]'''
            lineTemp=string.rstrip(line)
            lineTemp=string.split(lineTemp)
            
            if (username == lineTemp[0]):
                newVal = (int(lineTemp[1]) + increment)
                if (newVal < 0):
                    newVal = 0
                
                if (fileinput.filelineno() == lineCount):
                    newLine = lineTemp[0] + " " + str(newVal) + " " + datetime.strftime(getCurrentDateTime(), '%d/%m/%Y/%H:%M:%S')
                else:
                    newLine = lineTemp[0] + " " + str(newVal) + " " + datetime.strftime(getCurrentDateTime(), '%d/%m/%Y/%H:%M:%S') + "\n"
                line = line.replace(line,newLine)
                print(line, end='')
            else:
                print(line, end='')
                
    else:
        createdLine = "\n" + username + " " + str(increment) + " " + datetime.strftime(getCurrentDateTime(), '%d/%m/%Y/%H:%M:%S')
        dataFile = open(filename, 'a')
        dataFile.write(createdLine)