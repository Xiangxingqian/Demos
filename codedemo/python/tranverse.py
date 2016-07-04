import os

dir = 'E:\\benchmark'
suffix = '.apk'
dirs = []
		
def listallfile(tmpdir):
	if os.path.isdir(tmpdir):
		files = os.listdir(tmpdir)
		for f in files:
			file = tmpdir+os.sep+f
			if(os.path.isdir(file)):
				listallfile(file)
			else:
				if file.endswith(suffix):
					dirs.append(file)
				
listallfile(dir)
print dirs