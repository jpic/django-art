#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-art',
    version="0.0",
    author='James Pic',
    author_email='jamespic@gmail.com',
    description='Manage an art work collection in Django',
    url='http://github.com/jpic/django-art',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
    requires=[
        'django-mptt (>=0.5)',
    ],
    extras_require={
        'translation': [
            'django-modeltranslation',
        ]
    }
)
