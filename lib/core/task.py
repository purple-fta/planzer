from typing import Set, Any, Iterable
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from .tag import Tag


class Priority(Enum):
    low = 0
    normal = 1
    high = 2


@dataclass
class Task:
    """@dataclass with information about task

        Attributes:
            name (str): Name of task
            priority (Priority): 
            tags (Set[Tag]): 
            decor (Any): Color or any other information in any type
            deadline (datetime): time by which the task must be completed
    """
    name: str
    priority: Priority
    tags: Iterable[Tag]
    decor: Any
    deadline: datetime
