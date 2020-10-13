from shutil import copyfile
import os, stat

def install(globally):
	if globally:
		print("I should install myself globally")

	else:
		copyfile("grammaticommit/commit-msg", ".git/hooks/commit-msg")
		mode = os.stat('.git/hooks/commit-msg')
		os.chmod('.git/hooks/commit-msg', mode.st_mode | stat.S_IEXEC)
