from setuptools import setup


def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    name="grammaticommit",
    version="0.5",
    description="Fix your damn commit message grammar!",
    long_description=readme(),
    url="https://github.com/FdelMazo/grammaticommit",
    author="FdelMazo",
    # PyPi doesn't allow direct dependencies to be uploaded.
    # The real Pattern dependency is the one that works on Py3 > 3.6
    # That's being discussed in: https://github.com/clips/pattern/issues/62
    # The actual dependency should be:
    #     Pattern @ git+git://github.com/clips/pattern.git@17f215438166729114762c3d9b3179dacd31490d"
    install_requires=["termcolor>=1.1.0", "Pattern>=3.6"],
    packages=["grammaticommit"],
    python_requires=">3",
    package_data={"grammaticommit": ["commit-msg"]},
    scripts=["script/grammaticommit"],
    classifiers=["Programming Language :: Python :: 3"],
)
