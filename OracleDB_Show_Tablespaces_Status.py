########################################################################
#Script Connect To Oracle DB and Write Tablespaces Status Into Txt File#
########################################################################
import cx_Oracle

#Oracle DB Config
#Require DB Schema that has grant select on dba_data_files, dba_free_space and dba_temp_files views
conn= cx_Oracle.connect("<DB Schema Name>","<DB Password>","<Host Name>/<DB Instance Name>")

dir_path = str(input("Insert Target Directory For Output: for example: C:/TEST/ "))
#dir_path="C:/TEST/"

show_ts=str( "(select b.tablespace_name TS_NAME, round(tbs_size,2) TS_SIZE, round(a.free_space,2) FREE_MB, round(tbs_size - a.free_space, 2) USED_MB, round(a.free_space / tbs_size * 100 , 2) from (select tablespace_name, round(sum(bytes)/1024/1024 ,2) as free_space from dba_free_space group by tablespace_name) a, (select tablespace_name, sum(bytes)/1024/1024 as tbs_size from dba_data_files group by tablespace_name UNION select tablespace_name, sum(bytes)/1024/1024 tbs_size from dba_temp_files group by tablespace_name) b where a.tablespace_name(+)=b.tablespace_name) ")

print (show_ts)

#Connect To DB and Get Biggest Tables Info That More Than 100mb
c = conn.cursor()
c.execute(show_ts)
c2 = conn.cursor()
c2.execute('select INSTANCE_NAME from v$instance')

#Edit DB Name For Output Text File
db_name = str(c2.fetchone())
db_name=db_name.replace("(", "")
db_name=db_name.replace(")", "")
db_name=db_name.replace(",", "")
db_name=db_name.replace("\'", "")
print(db_name)

opt_file=str(db_name) + "_Tablespaces_Status.txt"
file_path=dir_path + opt_file

#Write Output Into Text File
f=open(dir_path + opt_file ,"w+")
f.write("DB Name: " + db_name + " \n" )
f.write("------------------------------------------------------------------------------------------------------------------------" + " \n")
f.write("| Tablespace Name      |         Tablespace Size                 |       Free MB       |     Used MB      |    % Free  |" + " \n")
f.close()
f=open(dir_path + opt_file ,"a+")
f.write("------------------------------------------------------------------------------------------------------------------------" + " \r\n")
f=open(dir_path + opt_file ,"a+")
for row in c:
    print (row)
    f.write('{: ^{width}}'.format(str(row[0]), width=30) + '{: ^{width}}'.format(str(row[1]), width=30)  + "      " + '{: ^{width}}'.format(str(row[2]), width=15) + "      " + '{: ^{width}}'.format(str(row[3]), width=15) + "      " + '{: ^{width}}'.format(str(row[4]), width=10) + "\n")
f.close()
