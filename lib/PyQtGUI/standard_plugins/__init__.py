import os

files_list = os.listdir("/home/baioretto/PROJECTS/planzer/lib/PyQtGUI/standard_plugins")

files_list.remove("__init__.py")
files_list.remove("__pycache__")

plugins_classes = []

for file_name in files_list:
    exec(f"import lib.PyQtGUI.standard_plugins.{file_name[:-3]}")
    exec(f"plugins_classes.append({file_name[:-3]}.plugin_class)")
