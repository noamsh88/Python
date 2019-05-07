from pymongo import MongoClient
import sys

"""
    script is copying all documents from source collection to target collection
"""

host = str(input("Please Insert Mongo Host in following format mongodb://hostname:port :"))
src_db  = str(input("Insert Source DB: "))
src_col = str(input("Insert Source Collection: "))
trg_db = str(input("Insert Target DB: "))
trg_col = str(input("Insert Target Collection: "))

#Mongo config
#host="mongodb://****:27017/"
myclient = MongoClient(str(host))
mydb = myclient["train_mongo"]

#src_db = 'train_mongo'
#trg_db = 'train_mongo'
#src_col = 'customer'
#trg_col = 'video'

#Check if given source and target DB are exist
def IfDBExist(src_db,trg_db):
    if bool(src_db not in myclient.list_database_names()):
        sys.exit("DB name " + src_db + " Not Exist ")
    else:
        if bool(trg_db not in myclient.list_database_names()):
            sys.exit("DB name " + trg_db + " Not Exist ")

#Copy all documents from source collection to target collection
def CopyFromColl1ToColl2(src_db,src_col,trg_db,trg_col):
    db1 = MongoClient(host)[src_db][src_col]
    db2 = MongoClient(host)[trg_db][trg_col]
    for doc in db1.find():
        try:
            db2.insert(doc)
            print(doc)
        except:
            print('following document did not copied ---> ' + str(doc))

#Main#
IfDBExist(src_db,trg_db)
CopyFromColl1ToColl2(src_db,src_col,trg_db,trg_col)
