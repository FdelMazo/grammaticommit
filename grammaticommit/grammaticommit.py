from shutil import copyfile
import os, stat
from subprocess import DEVNULL, call

module = os.path.abspath(os.path.dirname(__file__))
src = [module, "commit-msg"]
dst = [".git", "hooks", "commit-msg"]

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
			call(['git', 'config', '--global', 'core.hooksPath', os.path.join(module)])

	else:
		if not os.path.exists('.git'):
			print("This is not a local git repository!")
			print("Make sure you call `grammaticommit` from within the repository's root")
			return

		if os.path.exists(os.path.join(*dst)):
			print("You already have a commit-msg hook installed in this repository!")
			print(f"It is placed on {os.path.join(*dst)}")
			print("Delete it before installing grammaticommit!")
			return

		copyfile(os.path.join(*src), os.path.join(*dst))
		mode = os.stat(os.path.join(*dst))
		os.chmod(os.path.join(*dst), mode.st_mode | stat.S_IEXEC)

def uninstall(globally):
	if globally:
		call(['git', 'config', '--global', '--unset', 'core.hooksPath'])

	else:
		if not os.path.exists('.git'):
			print("This is not a local git repository!")
			print("Make sure you call `grammaticommit` from within the repository's root")
			return

		call(['git', 'config', 'core.hooksPath', os.path.join(*[".git", "hooks"])])

	if os.path.exists(os.path.join(*dst)) and os.path.getsize(os.path.join(*src)) == os.path.getsize(os.path.join(*dst)):
		os.remove(os.path.join(*dst))
