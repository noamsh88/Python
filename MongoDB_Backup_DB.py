from pymongo import MongoClient
import sys
import os


host_name = str(input("Please Insert Mongo Host in following format <hostname>:<port> :"))
db_name  = str(input("Insert DB Name to Backup: "))
bkp_dir_path = str(input("Insert Directory Path for Backup:  "))

"""
host_name = str('****:27017')
db_name = str('train_mongo')
bkp_dir_path='C:/TEST/MongoDB'
"""

"""
    Script is taking backup of Mongo DB using mongodump command
"""

client = MongoClient(host_name)

#Checks if Source DB name exist and exist the program in case not
def IfDBExist(db_name):
    if bool(db_name not in client.list_database_names()):
        sys.exit("DB name " + db_name + " Not Exist on " + host_name)

#takes Mongo DB backup for given DB name in backup directory
def BackupDB(host_name,db_name,bkp_dir_path):
    bkp_cmd = str("mongodump --host " + host_name + " --db " + db_name + " --out " + bkp_dir_path)
    print(bkp_cmd)
    os.system(bkp_cmd)

#Main#
IfDBExist(db_name)
BackupDB(host_name,db_name,bkp_dir_path)
