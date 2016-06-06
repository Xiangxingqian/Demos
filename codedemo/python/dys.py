import os
import sys
lines = os.popen('adb shell dumpsys activity').readlines()

list = [];

fp = open("L:\EHB\logger.txt",'r+')
for line in lines:
	if 'mFocusedActivity:' in line:	
		ss = line.split(' ')
		for s in ss:
			if 'cz.romario.opensudoku' in s:
				list.append(s)
				print list[0]
		print line
		 
