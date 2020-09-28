from setuptools import setup, find_packages

with open('README.rst',encoding = 'UTF-8') as f:
	readme = f.read()

setup(
    name='userlist',
    version='1.0.0',
    description='Command line user export utility',
    long_description= readme,
	url='https://github.com/jos3neto/userlist',
    author='Jose Neto',
    author_email='jose.neto@gmx.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
	entry_points={
        'console_scripts': 'userlist=userlist.cli:main'
    }
)
	