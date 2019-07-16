import os, sys, json
from mysql_handler import upload_data
import system_handler

def processSingle(jsonPath):
	#print(jsonPath, '\n')
	with open(jsonPath) as f:
		definitions = json.load(f)
	upload_data(definitions)

		



def processMultiple(dirClean, dirLog):
	#print('dirClean:', dirClean, 'dirLog:', dirLog)
	jsonList = system_handler.getFileFromFolder(dirClean)
	#print(jsonList)
	logData = []
	logPath = system_handler.getDatedFilePath(dirLog)
	for jsonPath in jsonList:
		processSingle(jsonPath)
		logData.append("Processed " + str(jsonPath))

	logData.append(system_handler.getDateStamp())
	system_handler.writeListToFile(logData, logPath)
	#print(logData)

	

	#print(logPath)




	system_handler.openDir(dirLog)
	sys.exit()