####################################################################
#Script Connect To Oracle DB and Write Biggest Tables Into Txt File#
####################################################################
import cx_Oracle

#Oracle DB Config
#Require DB Schema that has grant select on dba_segments and v$instance views
conn= cx_Oracle.connect("<DB Schema Name>","<DB Password>","<Host Name>/<DB Instance Name>")

dir_path = str(input("Insert Target Directory For Output, for example: C:/TEST/ : "))
#dir_path="C:/TEST/"

#Connect To DB and Get Biggest Tables Info That More Than 100mb
c = conn.cursor()
c.execute('SELECT owner, segment_name, tablespace_name, segment_type,  bytes/1024/1024 FROM dba_segments WHERE bytes/1024/1024 > 100 and segment_type=:segtype ORDER BY 5 DESC', {'segtype' : 'TABLE'})
c2 = conn.cursor()
c2.execute('select INSTANCE_NAME from v$instance')

#Edit DB Name For Output Text File
db_name = str(c2.fetchone())
db_name=db_name.replace("(", "")
db_name=db_name.replace(")", "")
db_name=db_name.replace(",", "")
db_name=db_name.replace("\'", "")
print(db_name)

opt_file=str(db_name) + "_Biggest_Tables.txt"
file_path=dir_path + opt_file

#Write Output Into Text File
f=open(dir_path + opt_file ,"w+")
f.write("DB Name: " + db_name + " \n" )
f.write("--------------------------------------------------------------------------------------------------" + " \n")
f.write("| Owner      |         Name                 |       TS Name       |     Type      |    Size in MB  |" + " \n")
f.close()
f=open(dir_path + opt_file ,"a+")
f.write("--------------------------------------------------------------------------------------------------" + " \r\n")
f=open(dir_path + opt_file ,"a+")
for row in c:
    print (row)
    f.write('{: ^{width}}'.format(str(row[0]), width=10) + '{: ^{width}}'.format(str(row[1]), width=30)  + "      " + '{: ^{width}}'.format(str(row[2]), width=15) + "      " + '{: ^{width}}'.format(str(row[3]), width=15) + "      " + '{: ^{width}}'.format(str(row[4]), width=10) + "\n")
f.close()
