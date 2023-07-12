import os.path
from typing import Any
import json




class SaveLoadSystem:
    """
    Класс для сохранения и загрузки информации от плагинов в .json файлы
    
    Args:
        file_name (str): Имя файла для записи. УНИКАЛЕН
        to_dict_func (function): Функция преобразующая информацию из классов в словарь, 
                                 который будет сохранён как JSON файл. Принимает args
        from_dict_func (function): Функция принимающая словарь и возвращающая исходную 
                                   информацию.
    """



    def __init__(self, file_name: str, to_dict_func: function, from_dict_func: function):
        pass

   # def to_dict_func(self, *args):


    def load(self) -> Any:

        # Визначаємо шлях до файлу JSON
        json_file_path = "file.json"

        # Відкриваємо файл у режимі читання
        with open(json_file_path, "r") as file:
            # Завантажуємо дані з файлу JSON
            data = json.load(file)   #dict

        return from_dict_func(data)
        """
        Возвращает результат из JSON переданный в from_dict_func

        """

    def save(self, args) -> None:
        path=""  #TODO
        file_name="" #TODO
        dict_data=to_dict_funk(data)
        with open(os.path.join(path,file_name),"w") as file:
            json.dump(dict_data,file)
        """
        Сохраняет словарь от to_dict_func с переданными args в JSON файл

        Args:
            args: Аргументы, что будут переданы в to_dict_func

        Raises:
            InvalidNumberOfArguments: если from_dict_func не принимает аргументы
        
        """
