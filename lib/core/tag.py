from dataclasses import dataclass
from typing import Any


@dataclass
class Tag:
    """
        @dataclass with information

        Params:
            name (str): Tag name
            decor (Any): Color or any other information in any type
    """
    name: str
    decor: Any

