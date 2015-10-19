from setuptools import setup, find_packages
from io import open
from os import path

with open(path.join(path.dirname(__file__), "README.md")) as readme:
    long_description = readme.read()

classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Software Developers in Test",
    'Topic :: Software Development :: Test Automation Tools',
    "License :: OSI Approved :: GNU License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
]

setup(
    name="xml2htmlreport",
    version='1.0.0a1',
    description="An implementation of converter JUnit XML reports into Responsive HTML report with screenshots and dashboard",
    long_description=long_description,
    url="http://github.com/KorolevskyMax/jUnitXML2HTML",
    author="Max Korolevsky",
    author_email="Korolevsky.Max@gmail.com",
    license="GNU",
    classifiers=classifiers,
    keywords='test automation tool',
    packages=["xml2htmlreport"],
    package_data={"xml2htmlreport": [
        "static/*/*.*",
        "static/font-awesome/*/*.*",
        "templates/*.*"
    ]},
    install_requires=["jinja2", "xmltodict", ],
    entry_points={"console_scripts": ["xml2htmlreport=xml2htmlreport.cli:main"]},
)
