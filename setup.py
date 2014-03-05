from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='ninfo-plugin-threatexpert',
    version=version,
    description="ThreatExpert hash lookup",
    keywords='',
    author='Justin Azoff',
    author_email='jazoff@illinois.edu',
    url='',
    license='',
    zip_safe=False,
    packages = find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        "ninfo",
    ],
    entry_points = {
        'ninfo.plugin': [
            'threatexpert    =   ninfo_plugin_threatexpert'
        ]
    }
) 
