import os, sys
import datetime

def openDir(targetdir):
	#open directory when done	
	rpath = os.path.realpath(targetdir)
	os.startfile(rpath)

def getDatedFilePath(dirOut):
	fileName = str(datetime.datetime.now())
	fileName = fileName.replace("-", "_")
	fileName = fileName.replace(":", "_")
	fileName = fileName.replace(".", "_")
	temp_path = "Google_to_MySQL_Log" + fileName + ".txt"
	pathOut =  os.path.join(dirOut, temp_path) 
	return(pathOut)

def getDateStamp():
	getDateStamp = str(datetime.datetime.now())
	getDateStamp = str("JSON to MySQL uploading completed at " + getDateStamp)

	return(getDateStamp)


	
def readTextFile(filepath):
	try:
	    ofile = open(filepath, 'r', encoding = 'utf-8') 
	    data = ofile.read()
	    return data
	except FileNotFoundError:
	    print("file not found")    
	except Exception as e:
	    print(e)  

def getMatchTuple(inPath):
	maps =  readTextFile(inPath)
	#turn map into tuple list
	tempList = maps.split('\n')
	matchList=[]
	for item in tempList:
		#print(item)
		if (item):
			match = item.split(',')
			#print(match[0], match[1])
			matchList.append((match[0], match[1]))
	return matchList

def getFileFromFolder(dirJSON):

	JSON_EXT = ".json"
	fileList = []

	for file in os.listdir(dirJSON):
	    if file.endswith(JSON_EXT):
	        fileList.append(os.path.join(dirJSON, file))

	return fileList

def writeListToFile(vlist, vpath):
    with open(vpath, 'w', encoding ='utf-8') as file:
        for item in vlist:    
            file.write(item + "\n")