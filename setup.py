# SET UP FILE:
# in order to run in notebooks as an import RockstarLifestyle
# 1. go to the outermost Rockstar_Lifestyle folder
# 2. use "pip install . "
# 3. import into a notebook using "from RockstarLifestyle import xxxxxx"

from setuptools import setup

setup(name = 'Rockstar_Lifestyle',
    version = '0.1',
    packages = ['rockstar_lifestyle'],
    url = 'https://github.com/hhelmbre/Rockstar-Lifestyle',
    license = 'MIT',
    author = 'Julia Boese, Hawley Helmbrecht, Sage Scheiwiller, David Shackelford',
    short_description = 'Protein image characterizer using Multi resolution histograms, object statistic, and edge statistics',
    long_description = open('README.MD').read(),
    zip_safe = False
)
