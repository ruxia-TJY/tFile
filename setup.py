# -*- coding: utf-8 -*-
from setuptools import setup,find_packages

with open("README.md",'r',encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tFile',
    version='0.0.1',
    keywords='File,OS',
    description='Encapsulate common file processing functions',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="ruxia-TJY",
    author_email="ruxia.tjy@qq.com",
    url="https://github.com/ruxia-TJY/tFile",
    download_url="https://github.com/ruxia-TJY/tFile",
    project_urls={
        "Bug Tracker":"https://github.com/ruxia-TJY/tFile/issues",
    },
    install_requires=[],
    packages=find_packages(),
    license='MIT',
    python_requires='>=3',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'License :: OSI Approved :: BSD License'
    ]
)