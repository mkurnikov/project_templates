from __future__ import division, print_function

from setuptools import setup, find_packages


setup(
    name='kaggle_template',
    version='0.0.1.dev1',
    author="Maxim Kurnikov",
    author_email="maxim.kurnikov@gmail.com",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'makeproject = makeproject.makeproject:run'
        ]
    }
)
