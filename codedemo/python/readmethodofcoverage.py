import os
import sys
import re

result=[]
def readFile(file, appname):
	line = open(file,'r').read()
	m = re.findall(r'(\w*[0-9]+)\w*',line)
	print appname, m

root = "C:\Users\lenovo\workspace\EHBDroid\output"
files = os.listdir(root) 
for file in files:
	t = root+"\\"+file
	texts = os.listdir(t)
	for text in texts:
		if text.endswith('_moc.txt'):
			readFile(t+"\\"+text, file)


