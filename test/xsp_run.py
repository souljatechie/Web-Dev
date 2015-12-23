import os
from subprocess import call
#call(["ps", "-f", "|", "grep", "xsp_run.py"])
#call (["xsp4 --port 8080"])

#os.system("echo starting  xsp4 --port 8080")
#os.system("xsp4 --port 8080")
#print 'command complete'


#mpid = os.getpgrp('mono')
#print mpid


#cwd = os.getcwd()

count =1

while count > 0:
	try:
		os.system("echo starting  xsp4 --port 8080")
		os.system("xsp4 --port 8080")
		print 'command complete'

	except:
		print 'error, danger will robinson, danger'

#os.execl('/var/www/html/test', 'xsp4 --port 8080') 

#os.fdopen ('xsp4 --port 8080','w')

