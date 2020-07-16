import os
pwd = "탐색할 디렉터리 경로"
for path, dirs, files in os.walk(pwd):
	for file in files:
		if os.path.splitext(file)[1].lower() == '.txt':
			print 'txt 파일: ' + file
