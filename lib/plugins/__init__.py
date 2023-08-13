""" To get a list of files in a directory """
import os


folder_list = os.listdir("/home/baioretto/PROJECTS/planzer/lib/plugins")

# TODO: Нужно удалить всё кроме папок плагинов автоматически, а не вручную
folder_list.remove("__init__.py")
folder_list.remove("__pycache__")

plugins_classes = []

for folder_name in folder_list:
    exec(f"import lib.plugins.{folder_name}")
    exec(f"plugins_classes.append({folder_name}.plugin_class)")
