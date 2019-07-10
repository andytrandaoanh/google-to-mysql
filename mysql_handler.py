import os, sys
import mysql.connector
from mysql.connector import errorcode

def get_connection(dbname=''):
	try:
		connection = mysql.connector.connect(
		user='andyanh', password='DGandyanh#1234',
	    host='127.0.0.1', database = dbname)
		if connection.is_connected():
			return connection 
	except Error as e:
		return e




def insert_row_to_database(myData, cursor, db):

	mySql = ("INSERT INTO google_defs "
	           "(word, phonetic, category, definition, date_enter)"
	           "VALUES (%s, %s, %s, %s, NOW())")

	try:
		cursor.execute(mySql, myData)
	except Exception as e:
		print("Error encountered:", e)
	
	db.commit()




def upload_data(defData):
	#print('bookID:', bookID)
	#print('mapData:', mapData)

	dataList = []
	for defItem in defData:
		if(defItem):
			#print(defItem)
			tup = (defItem['word'], defItem['phonetic'], defItem['category'], defItem['definition'])
			dataList.append(tup)
	
	
	#print(dataList)
	DB_NAME = "lexicon"

	db = get_connection(DB_NAME)

	cursor = db.cursor()
	for item in dataList:
		insert_row_to_database(item, cursor, db)
		print('uploading...', item)

	cursor.close()

	db.close()