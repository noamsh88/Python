from pymongo import MongoClient
import sys

"""
server_name = str(input("Please Insert Mongo Host with following format mongodb://hostname:port :"))
src_db  = str(input("Insert Source DB: "))
trg_db = str(input("Insert Target DB: "))
"""
server_name = str('mongodb://illin4040:27017')
src_db = str('train_mongo')
trg_db = str('train_mongo2')


"""
    Script is duplicating source Mongo DB to new one
"""

myclient = MongoClient(server_name)

#Checks if Source DB name exist and exist the program in case not
def IfDBExist(src_db):
    if bool(src_db not in myclient.list_database_names()):
        sys.exit("DB name " + src_db + " Not Exist ")

#Function is Duplicating Source DB to Target DB name
def DuplicateDB(server_name,src_db,trg_db):
    try:
        myclient.admin.command('copydb',fromdb=src_db,todb=trg_db)
    except:
        print('Copy failed')



IfDBExist(src_db)
DuplicateDB(server_name,src_db,trg_db)
