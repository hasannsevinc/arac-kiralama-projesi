# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 18:10:45 2023

@author: karaci
"""

from PyQt5 import uic

with open("menuui.py",'w', encoding="utf-8") as fout:
    uic.compileUi("menu.ui", fout)