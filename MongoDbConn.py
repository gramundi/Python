from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint


def recordDetection(obj):
	# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
	client = MongoClient("mongodb://not001328:27017")
	#Choose DB
	db=client.vision
	#Choose Collection and store the document
	detectionstore=db.dataset
	detectionstore.insert(obj)
	return 