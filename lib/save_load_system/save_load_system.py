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
        pass  # TODO: Что бы использовать file_name, to_dict_func и from_dict_func нужно использовать self


    def load(self) -> Any:
        # TODO: """ Вот такой комментарий с """ должен быть в начале, а не в конце. 
        #           Это описание функции и того, что в ней будет происходить """

        # Визначаємо шлях до файлу JSON
        json_file_path = "file.json"  # TODO: нужно использовать file_name из конструктора класса 

        # Відкриваємо файл у режимі читання
        with open(json_file_path, "r") as file:
            # Завантажуємо дані з файлу JSON
            data = json.load(file)   #dict

        return from_dict_func(data) # TODO: from_dict_func нужно сохранить в self.from_dict_func
        """
        Возвращает результат из JSON переданный в from_dict_func

        """

    def save(self, args) -> None:
        # TODO: Тут в начале должен быть многострочный комментарий, который сейчас в конце
         
        path=""  #TODO
        file_name="" # TODO: нужно использовать file_name из self
        dict_data=to_dict_funk(data) # TODO: тоже из self нужно брать
        with open(os.path.join(path,file_name),"w") as file:
            json.dump(dict_data,file)
        """
        Сохраняет словарь от to_dict_func с переданными args в JSON файл

        Args:
            args: Аргументы, что будут переданы в to_dict_func

        Raises:
            InvalidNumberOfArguments: если from_dict_func не принимает аргументы
        
        """
