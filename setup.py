import ast
import os
import re
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('pretty_json/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(
        _version_re.search(f.read().decode('utf-8')).group(1)
    ))

setup(
    name='pretty-json',
    packages=[
        'pretty_json'
    ],
    version=version,
    include_package_data=True,
    description='make pretty json',
    long_description=open('README.rst').read(),
    url='https://github.com/devstuff-io/pretty-json',
    author='meganlkm',
    author_email='devstuff.io@gmail.com',
    install_requires=[
        'Pygments',
        'pygments-json'
    ],
    keywords=[
        'pretty',
        'json'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
