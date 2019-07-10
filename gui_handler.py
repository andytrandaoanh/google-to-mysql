import json
from mysql_handler import upload_data

def prepareUpload(jsonPath):
	#print(inPath)
	with open(jsonPath) as f:
		definitions = json.load(f)
	upload_data(definitions)
		
