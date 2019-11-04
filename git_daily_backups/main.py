
import os, time

# Variable Declaration #
clone= 'git clone https://github.com/eagleinvsys-sd/sd-core-17 .' # Command to clone a specific remote repository #
pull = 'git pull origin' # Command to update the existing repository #
newFld = 'F:/SD-CORE-17-BACKUPS/' + time.strftime("%m_%d_%y") # Give path and create a folder with today's date #

# Check if a backup for today exists and if so perform a Pull to update the repo #
if os.path.isdir(newFld):
	print("Backup repository already exists.  Will perform a PULL")
	os.chdir(newFld)
	os.system(pull)
# If backup for today doesn't exist then create a new forlder with today's date then clone the remote repository #
else:
	print("Backup repository doesn't exists.  Will perform a CLONE")
	os.makedirs(newFld)
	os.chdir(newFld)
	# os.system('git-lfs install')
	os.system(clone)
