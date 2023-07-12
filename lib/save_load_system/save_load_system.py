from typing import Any


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

    def load(self) -> Any:
        """
        Возвращает результат из JSON переданный в from_dict_func

        """

    def save(self, args) -> None:
        """
        Сохраняет словарь от to_dict_func с переданными args в JSON файл

        Args:
            args: Аргументы, что будут переданы в to_dict_func

        Raises:
            InvalidNumberOfArguments: если from_dict_func не принимает аргументы
        
        """
