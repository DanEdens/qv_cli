"""
    init file for Join-CLi 
"""
# __name__ = 'join'


import os
import sys
import datetime


today = datetime.datetime.now()

# Clearly defines the project root
os.environ['ROOT_DIR'] = os.path.dirname(os.path.abspath(__file__))

os.environ['filedate'] = today.strftime("%Y-%m-%d")
os.environ['Nowdate'] = today.strftime("%Y-%m-%d %H:%M:%S")

sys.path.insert(0, os.environ['ROOT_DIR'])
# print(os.environ['ROOT_DIR'])
