import os

from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    long_description = readme.read()

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
]

setup(
    name="xml2htmlreport",
    packages=["xml2htmlreport", "xml2htmlreport.tests"],
    package_data={"xml2htmlreport": ["static/*.*" , "templates/*.*"]},
    setup_requires=["vcversioner", "jinja2", "xmltodict", ],
    author="Max Korolevsky",
    author_email="Korolevsky.Max@gmail.com",
    classifiers=classifiers,
    description="An implementation of converter JUnit XML reports into Responsive HTML report with screenshots and dashboard",
    license="GNU",
    long_description=long_description,
    url="http://github.com/KorolevskyMax/jUnitXML2HTML",
    entry_points={"console_scripts": ["xml2htmlreport = xml2htmlreport.cli:main"]},
    vcversioner={"version_module_paths" : ["xml2htmlreport/_version.py"]},
)