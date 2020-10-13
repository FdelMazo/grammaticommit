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
	  packages=['grammaticommit'],
	  package_data={'grammaticommit': ['commit-msg']},
	  scripts=['script/grammaticommit'],
	  classifiers=[
		  'Programming Language :: Python :: 2',
		  'Programming Language :: Python :: 3'
	  ]
)
