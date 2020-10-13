from shutil import copyfile
import os, stat
from subprocess import DEVNULL, call

module = os.path.abspath(os.path.dirname(__file__))
src = [module, "commit-msg"]
local_dst = [".git", "hooks", "commit-msg"]

def install(globally):
	if globally:
		globalhooks = call(['git', 'config', '--global', 'core.hooksPath'], stdout=DEVNULL)
		if globalhooks == 0:
			print("You already have global hooks directory set")
			print("You should just copy and paste the commit-msg hook yourself instead of me overwriting it")
			print(f"The commit-msg hook is placed on:\n\t{os.path.join(*src)}")
			print("Your global hooks directory is:", end='\n\t')
			call(['git', 'config', '--global', 'core.hooksPath'])

	else:
		if not os.path.exists('.git'):
			print("This is not a local git repository!")
			print("Make sure you call `grammaticommit` from within the repository's root")
			return

		if os.path.exists(os.path.join(*local_dst)):
			print("You already have a commit-msg hook installed in this repository!")
			print(f"It is placed on {os.path.join(*local_dst)}")
			print("Delete it before installing grammaticommit!")
			return

		copyfile(os.path.join(*src), os.path.join(*local_dst))
		mode = os.stat(os.path.join(*local_dst))
		os.chmod(os.path.join(*local_dst), mode.st_mode | stat.S_IEXEC)
