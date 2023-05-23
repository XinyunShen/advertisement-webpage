"""
nearal python package configuration.

Xinyun Shen
"""

from setuptools import setup

setup(
    name='nearal',
    version='0.1.0',
    packages=['nearal'],
    include_package_data=True,
    install_requires=[
        'arrow==0.15.7',
        'bs4==0.0.1',
        'Flask==1.1.2',
        'html5validator==0.3.3',
        'pycodestyle==2.6.0',
        'pydocstyle==5.0.2',
        'pylint==2.5.3',
        'pytest==5.4.3',
        'requests==2.31.0',
    ],
    python_requires='>=3.6',
)
