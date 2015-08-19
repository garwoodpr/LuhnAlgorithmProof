
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Luhn Algorithm Validator -- long description
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='luhn_algorithm_validator',

    version='1.0.1',

    packages = ['luhn'],

    description='Luhn Account Number Validator',
    long_description=long_description,

    # Project homepage
    url='https://github.com/garwoodpr/LuhnAlgorithmProof',

    # Author details
    author='Clint Garwood',
    author_email='clint@garwoodpr.com',

    # License
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for

        'Topic :: Text Processing :: General',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Office/Business :: Financial',
        'Programming Language :: Python :: 3.4', 
        'Operating System :: OS Independent', 
        'Natural Language :: English', 
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Customer Service', 
    ],

    keywords=['Luhn Algorithm', 'account number validation', 'credit card validation', 'text analysis', 'information processing', 'data verification', 'cryptography', 'numerical decoding',
    ],

)

