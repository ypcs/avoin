# -*- coding: utf-8 -*-

__package_name = 'avoin'

import os
from setuptools import setup, find_packages
from version import get_git_version

def read(filename):
    f = os.path.join(os.path.dirname(__file__), filename)
    if os.path.exists(f):
        return open(f).read()

setup(name=__package_name,
    version = get_git_version(),
    description='Misc python tools',
    long_description=read('README.md'),
    author='Ville Korhonen',
    author_email='ville@xd.fi',
    url='https://github.com/ypcs/' + __package_name,
    packages=find_packages('src'),
    package_dir={'': 'src',},
    install_requires=[
        'requests',
        'requests_cache',
        'lxml',
        'pymongo',
    ],
    license='GPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        ],
    entry_points={
        'console_scripts': [
            'avoin = avoin.core:run',
        ],
    },
)
