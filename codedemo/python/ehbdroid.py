from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By
import os
import sys

la = (80,380)
lb = (80,440)
ra = (240,380)

map = {'cz.romario.opensudoku/.gui.FolderListActivity': la, 
'cz.romario.opensudoku/.gui.SudokuListActivity': la, 
'cz.romario.opensudoku/.gui.SudokuPlayActivity': ra, 
'cz.romario.opensudoku/.gui.GameSettingsActivity': lb, 
'cz.romario.opensudoku/.gui.SudokuEditActivity': ra, 
'cz.romario.opensudoku/.gui.SudokuExportActivity': lb, 'cz.romario.opensudoku/.gui.FileListActivity': lb,
'cz.romario.opensudoku/.gui.FileImportActivity': lb,
'cz.romario.opensudoku/.gui.ImportSudokuActivity': lb,
'cz.romario.opensudoku/.gui.SudokuImportActivity': lb}

list = [];
app = 'cz.romario.opensudoku'
androidPackage = 'com.android.launcher'

easy_device = MonkeyRunner.waitForConnection()     

def clickMenu(position):
	easy_device.press('KEYCODE_MENU',MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(1.5)
	easy_device.touch(position[0],position[1],MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(8.0)

def clickBack():
	easy_device.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(3.0)

def dsy():
	line = os.popen('adb shell dumpsys activity').read()
	stack1 = line.split('Stack #1')[-1]
	activities = collectActivityInStack1(stack1)
	if contain(app, activities):
		if app in activities[0]:
			if activities[0] in list:
				return False
			else: 
				list.append(activities[0])
				return True
		else:
			return False
	else:
		writeFile()
		writeFile2()
		sys.exit(0)	

def isCurrentApp(appPackage, currentActivity):
	s = currentActivity[-2]
	if appPackage in s:
		print 55, appPackage, s
		if s in list:
			return False
		else: 
			list.append(s)
			return True
	else: 
		print 62, appPackage, s
		return False 

	
def getActivityName(qName):
	sep = qName.split('.')
	return sep[-1]
	
def writeFile():
	fp = open("L:\EHB\logger.txt",'w+')				
	for i in list:
		fp.write(i)
		fp.write("\n")
	fp.close()

def writeFile2():
	f = open("L:\EHB\events.txt",'w+')		
	f.write(os.popen('adb logcat -s -d EVENT:*').read())
	f.close()	

def collectActivityInStack1(stack1):
	activities = []
	lines = stack1.split('\n')
	for line in lines:
		if 'Run #' in line:
			activities.append(line.split(' ')[-2])
	return activities

def contain(appName, activities):
	for act in activities:
		if appName in act:
			return True
	return False
	
while 1:
	if dsy():
		clickMenu(map[list[-1]])
		print 'currentActivity', list[-1]
	else: 
		clickBack()
		