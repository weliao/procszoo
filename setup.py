#!/usr/bin/env python
import os
import sys
from distutils.log import warn as printf
from setuptools import setup, find_packages, Extension, Command

if 'build' in sys.argv:
    os.system('make')

setup(
    name='procszoo',
    version='0.97.1',
    description='python module to operate Linux namespaces',
    license='GPL2+',
    author='xning',
    author_email='anzhou94@gmail.com',
    packages = find_packages(),
    url='https://github.com/xning/procszoo',
    use_2to3=False,
    scripts=['bin/richard_parker', 'lib/procszoo/my_init'],
    ext_modules = [
        Extension('procszoo.c_functions.atfork',
                  ['procszoo/c_functions/atfork/atfork.c',
                   'procszoo/c_functions/atfork/atfork_module.c'],
                  include_dirs=['procszoo/c_functions/atfork']),
    ],
    package_data = {'': ['*.txt', '*.md', 'README.first']}
)
