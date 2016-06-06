import sys
import os
import time

times = "0"  

def writeFile():
	s = "L:\ehbexpriment"+"\\"+sys.argv[1]+times+".txt" 
	f = open(s,'w+')		
	f.write(os.popen('adb logcat -s -d EVENT:*').read())
	f.close()

for i in ["5","10","15"]:
	times = i
	time.sleep(300)
	writeFile()