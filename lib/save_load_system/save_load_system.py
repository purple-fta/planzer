import os.path
from typing import Any, Callable
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

    def __init__(self, file_name: str, to_dict_func: Callable, from_dict_func: Callable):
        self.file_name=file_name
        self.to_dict_func=to_dict_func
        self.from_dict_func=from_dict_func


    def load(self) -> Any:
        """
        Возвращает результат из JSON переданный в from_dict_func
        """

        # Визначаємо шлях до файлу JSON
        json_file_path = self.file_name

        # Відкриваємо файл у режимі читання
        with open(json_file_path, "r") as file:
            # Завантажуємо дані з файлу JSON
            data = json.load(file)   #dict

        return self.from_dict_func(data)


    def save(self, args) -> None:
        """
        Сохраняет словарь от to_dict_func с переданными args в JSON файл

        Args:
            args: Аргументы, что будут переданы в to_dict_func

        # TODO: Нужно переместить комментарии о Raises в описание класса после Args. В конструкторе нужно используя signature из inspect (Документация - https://docs.python.org/3/library/inspect.html#inspect.signature) проверить принимаемые аргументы и в случае чего вызвать исключение InvalidNumberOfArguments
        Raises:
            InvalidNumberOfArguments: если from_dict_func не принимает аргументы
        """
         
        path = ""  #TODO
        file_name = self.file_name 
        dict_data = self.to_dict_func(args)

        with open(os.path.join(path, file_name), "w") as file:
            json.dump(dict_data, file)
