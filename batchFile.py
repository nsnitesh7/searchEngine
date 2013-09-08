#!/usr/bin/python
import os.path
import sys

param=sys.argv
cacmfile = open(param[1], "r").readlines()

def check(pattern,line):
	if pattern[0] is line[0] and pattern[1] is line[1]:
		return True
	return False

parseoutputfile1 = open("testCollection.txt","w")
print "Parsing "+param[1]+" collection...."
flag = 0;
for line in cacmfile:
   if check(".I",line.strip()):
       line = line.split()
       if flag != 0:
          parseoutputfile1.write("</text>\n")
          parseoutputfile1.write("</page>\n\n")
       flag=1
       parseoutputfile1.write("<page>\n")
       parseoutputfile1.write("<id>")
       parseoutputfile1.write(line[1])
       parseoutputfile1.write("</id>\n")
   elif check(".T",line):
       count = 1;
       parseoutputfile1.write("<title>")
       pass
   elif check(".B",line):
       pass
   elif check(".A",line):
       pass
   elif check(".N",line):
       pass
   elif check(".W",line):
       pass
   elif check(".K",line):
       pass
   elif check(".C",line):
       pass
   elif check(".X",line):
       pass
   elif line.startswith(tuple('0123456789')):
       pass
   else:
       if count==1:
   	     parseoutputfile1.write(line[:len(line)-1] +"</title>\n")
   	     #parseoutputfile1.write()
   	     parseoutputfile1.write("<text>\n")
   	     count=0;
       else:
   	     parseoutputfile1.write(line)
parseoutputfile1.write("</text>\n")
parseoutputfile1.write("</page>\n\n")
parseoutputfile1.close()
print ""
print "------------------------------------------------------------------------------------------------------------------------------"
print "XML file generated."
print "------------------------------------------------------------------------------------------------------------------------------"
print ""

