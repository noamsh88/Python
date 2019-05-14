####################################################################
#Script:                                                           #
#1. connecting to given mongoDB                                    #
#2. send in mail list of available DB names and list of Collections#
####################################################################
import pymongo
from mailjet_rest import Client

#Mailjet config
api_key = '<Mailjet API Key>'
api_secret = '<Mailjet Secret Key>'
mailjet = Client(auth=(api_key, api_secret))
#Mongo config
host_name = str(input("Please Insert Mongo Host in following format mongodb://hostname:port :"))
db_name  = str(input("Insert DB Name: "))

myclient = pymongo.MongoClient(host_name)
mydb = myclient[mydb]
#myclient = pymongo.MongoClient("mongodb://****:27017/")
#mydb = myclient["train_mongo"]

print("DB Names: ")
print(myclient.list_database_names())
print("Collection names in train_mongo DB:")
print(mydb.list_collection_names())

avl_db_names = myclient.list_database_names()
avl_col_names = mydb.list_collection_names()

data = {
  'FromEmail': '<Insert From Mail>',
  'FromName': '<Insert From Name>',
  'Subject': 'Available DB Names:', #Subject
  #'TextPart': 'Follwing are available DB names:' + str(avl_db_names),
  'Html-part': '<h3>Available DB names: </h3>' + str(avl_db_names)
                + '<h3>Available Collection names: </h3>' + str(avl_col_names),
  'Recipients': [{ "Email": "<Insert Target Email"}]
}
result = mailjet.send.create(data=data)
print (result.status_code)
print (result.json())
