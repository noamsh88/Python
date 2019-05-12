##########################################################
#Script is restoring given Mongo DB from backup directory#
##########################################################
from pymongo import MongoClient
import sys
import os

host_name = str(input("Please Insert Mongo Host in following format <hostname>:<port> :"))
db_name  = str(input("Insert DB Name to Restore: "))
bkp_dir_path = str(input("Insert Directory Path of Backup:  "))

"""
host_name = str('***:27017')
db_name = str('train_mongo')
bkp_dir_path='C:/TEST/MongoDB/train_mongo'
"""

client = MongoClient(host_name)

#restore Mongo DB from backup directory
def RestoreDBFromBackup(host_name,db_name,bkp_dir_path):
    bkp_cmd = str("mongorestore --host " + host_name + " --db " + db_name + " " + bkp_dir_path)
    print(bkp_cmd)
    os.system(bkp_cmd)


#Main#
RestoreDBFromBackup(host_name,db_name,bkp_dir_path)
