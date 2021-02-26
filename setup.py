import sys
import getopt
import platform
import shutil
from pathlib import Path

from setuptools import setup, find_packages

PROJECT = 'sitecheck'
VERSION = ''
UPLOAD = ''
AUTHOR = 'Dan.Edens'

try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["version=", "upload="])
except getopt.GetoptError:
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print('python setup.py -v <version number>')
        sys.exit()
    elif opt in ("-v", "--version"):
        VERSION = arg

if Path.is_dir(Path('build')):
    print("Cleaning up previous build..")
    shutil.rmtree("build", ignore_errors=True)
    shutil.rmtree("dist", ignore_errors=True)
    shutil.rmtree("sitecheck.egg-info", ignore_errors=True)

with open(f"{PROJECT}/docs/README.md", "r") as fh:
    long_description = fh.read()

system = platform.system()

scripts = ['sitecheck/bin/scanner.sh', 'sitecheck/bin/scanner-config.sh', 
           'sitecheck/bin/scanner.cmd', 'sitecheck/bin/scanner-config.cmd']

setup(
    name=f'{PROJECT}',
    version=f'{VERSION}',
    description='Sitecheck toolkit for Geo-Instruments',
    long_description='Sitecheck toolkit for Geo-Instruments',
    author=f'{AUTHOR}',
    author_email='Dan.Edens@geo-instruments.com',
    url='https://github.com/DanEdens/Sitecheck_Scrapper',
    packages=find_packages(),
    scripts=scripts,
    script_args=["bdist_wheel"],
    license='',
    keywords=[""],
    include_package_data=True,
    package_data={
        "": ["*.cmd", "*.md", "*.ini", "*.png",
             "*.jpg", "*.json", "*.url", "*.zip"]
        },
    setup_requires=[
        "appdirs >= 1.4.4",
        "pyee >= 7.0.2",
        "pyppeteer >= 0.2.2",
        "python-dateutil >= 2.8.1",
        "six >= 1.10.0",
        "urllib3 >= 1.25.9",
        "websockets >= 8.1",
        "texttable >=1.6.2"
        ],
    install_requires=[
        "appdirs >= 1.4.4",
        "pyee >= 7.0.2",
        "pyppeteer >= 0.2.2",
        "python-dateutil >= 2.8.1",
        "six >= 1.10.0",
        "urllib3 >= 1.25.9",
        "websockets >= 8.1",
        "texttable >=1.6.2"
        ],
    python_requires='>=3.7'
    )
