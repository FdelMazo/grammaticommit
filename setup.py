from setuptools import setup

def readme():
	with open('README.rst') as f:
		return f.read()


setup(name='grammaticommit',
	  version='0.1',
	  description='Fix your damn commit message grammar!',
	  long_description=readme(),
	  url='https://github.com/FdelMazo/grammaticommit',
	  author='FdelMazo',
	  install_requires=['termcolor>=1.1.0', 'Pattern>=3.6'],
	  packages=['grammaticommit'],
	  package_data={'grammaticommit': ['commit-msg']},
	  scripts=['script/grammaticommit'],
	  classifiers=[
		  'Programming Language :: Python :: 3.6'
	  ]
)
