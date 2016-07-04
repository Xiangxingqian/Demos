import os

dir = 'E:\\benchmark'
suffix = '.apk'
dirs = []
		
def listallfile(tmpdir):
	if os.path.isdir(tmpdir):
		files = os.listdir(tmpdir)
		for f in files:
			dirs.append(f)
listallfile(dir)
print dirs