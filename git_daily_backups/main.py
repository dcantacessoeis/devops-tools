
import os, time

clone= 'git clone https://github.com/eagleinvsys-sd/sd-core-17 .'
pull = 'git pull origin'
newFld = 'F:/SD-CORE-17-BACKUPS/' + time.strftime("%m_%d_%y")

if os.path.isdir(newFld):
	print("Backup repository already exists.  Will perform a PULL")
	os.chdir(newFld)
	os.system(pull)
else:
	print("Backup repository doesn't exists.  Will perform a CLONE")
	os.makedirs(newFld)
	os.chdir(newFld)
	# os.system('git-lfs install')
	os.system(clone)
