import os
#line = os.system('ipconfig')
#print "finish"

map = {'FolderListActivity': (600,800), 'Age': 7, 'Class': 'First'};

tuple = map['FolderListActivity']
print tuple[0], tuple[1] 

lines = os.popen('ipconfig').readlines()
for line in lines:
	if 'DNS' in line:
		print line,
		

line = os.popen('ipconfig').read()
s = line.split('DNS')

lns = line.split('DNS')[-1].split('\n')[1]
print lns

def writeFile2():
	f = open("L:\EHB\events.txt",'w+')	
	f.write(os.popen('adb logcat -s -d EVENT:*').read())
	f.close()	

writeFile2()