#!/usr/bin/env python3
import os, setuptools

setup_path = os.path.dirname(__file__)

with open(os.path.join(setup_path, "README.md")) as readme:
    long_description = readme.read()

setuptools.setup(
    name="redesigned_journey",
    version="0.1",
    author="SciELO Dev Team",
    author_email="scielo-dev@googlegroups.com",
    description="Extract data for XC pid manager v3.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="2-clause BSD",
    packages=setuptools.find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests", "docs"]
    ),
    include_package_data=False,
    python_requires=">=3.7",
    install_requires=[
        "mongoengine",
        "tenacity",
    ],
    test_suite="tests",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Other Environment",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
    ],
)
