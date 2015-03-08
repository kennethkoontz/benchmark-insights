# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='benchmark-insights',
    version='0.0.1',
    author=u'Ken Koontz',
    author_email='kenneth.koontz@gmail.com',
    packages=find_packages(),
    license='MIT licence, see LICENCE.txt',
    url='https://github.com/usebenchmark/benchmark-insights.git',
    description="Benchmark's insight engine",
    long_description=open('README.rst').read(),
    zip_safe=False,
)
