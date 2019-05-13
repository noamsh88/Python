###########################################################################
#script is reading from given file name and count appearances of each word#
###########################################################################
import os

file_path = str(input("Please Enter Text File Location: "))
#file_path="C:/TEST/1.txt"

file=open(file_path,"r+")

wordcount={}

#Count appearances of each word in file
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

#Sort the result by count of appearance
wordcount = dict(sorted(wordcount.items(), key=lambda x: x[1]))

for k,v in wordcount.items():
    print (k, v)

#Write output into Text file
"""
output_path=dir_path + "output" + opt_file
f=open(output_path ,"a+")
for k,v in wordcount.items():
    #print (k, v)
    f.write(str(k) + "   " + str(v) + "\n")
"""
