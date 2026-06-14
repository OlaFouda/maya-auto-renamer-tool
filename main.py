""""
Tool Description: Auto Renaming Tool For Maya
Version: 1.0
Date: 2026-01-20
"""

from Renaming_Tool.ui import gui

import importlib

importlib.reload(gui)

gui.auto_renaming_gui()
