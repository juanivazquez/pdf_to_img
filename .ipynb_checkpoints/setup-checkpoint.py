#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module sets up the package for the lib_work_login"""

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(    
    name="pdfwidgets",
    # author="Juan Ignacio Vázquez Broquá",
    # author_email="juanivazquez@gmail.com",
    # maintainer="Juan Ignacio Vázquez Broquá",
    # maintainer_email="juanivazquez@gmail.com",
    version="0.0.0",
    # url="https://github.com/juanivazquez/pdf_to_img.git",
    # download_url='https://github.com/juanivazquez/pdf_to_img.git',
    # keywords=['JIVB', 'pdf', 'img', 'conversion'],
    license="BSD",
    description="Converts pdf file to a pdf file where each file is a pdf image",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    # project_urls={
    #    "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    # },
    # python_requires=">=3.6",
    packages=find_packages(),
    # include_package_data=True,
    install_requires=[
        'pillow==10.4.0',
        'fitz==0.0.1.dev2',
        'pynput==1.7.7',
        'setuptools==69.2.0'
    ],
    # classifiers=[
    #     'Environment :: Console',
    #     'Environment :: Web Environment',
    #     'Intended Audience :: Developers',
    #     'License :: OSI Approved :: BSD License',
    #     'Operating System :: POSIX :: Linux',
    #     'Programming Language :: Python :: 3'],
    # entry_points={
    #     'console_scripts': [
    #         'login = lib_work_login.__main__:main',
    #         'configure = lib_work_login.__main__:configure',
    #     ]},
    # setup_requires=['pytest-runner'],
    # tests_require=['pytest'],
)