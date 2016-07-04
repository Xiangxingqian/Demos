from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By
import os
import sys

la = (80,380)
lb = (80,440)
ra = (240,380)
view1 = (719,100)
view2 = (629,261)

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

def clickposition(position):
	easy_device.touch(position[0],position[1],MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(2.0)
def clickback():
	easy_device.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)
	result=easy_device.takeSnapshot()
	result.writeToFile('result1.png','png')
	MonkeyRunner.sleep(5.0)
	
for i in range(1,5):	
	clickposition(view1)
	clickposition(view2)
	clickback()
	