from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='pam2',
      version=version,
      description="PAM interface using ctypes",
      long_description="""\
An interface to the Pluggable Authentication Modules (PAM) library on linux, written in pure python (using ctypes)""",
      classifiers=["Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Operating System :: POSIX :: Linux",
          "Operating System :: MacOS :: MacOS X",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: System :: Systems Administration :: Authentication/Directory"
          ],
      keywords='',
      author='Grzegorz Nosek',
      author_email='root@localdomain.pl',
      url='http://github.com/gnosek/python-pam',
      download_url = "http://github.com/gnosek/python-pam/archive/%s.zip" % version,
      license='MIT',
      py_modules=["pam"],
      zip_safe=True,
      install_requires=[],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
