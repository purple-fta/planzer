from dataclasses import dataclass
from typing import Set, Iterable
from datetime import date
from enum import Enum


from .event import Event, EventOptions, StartEnd, StartDuration, EndDuration
from .timeline import Timeline
from .task import Task
from .tag import Tag


class SortBy(Enum):
    closest_to_deadline = 1
    sort_by_creation_age = 2 # TODO


@dataclass
class TaskListDisplayOptions:
    """
    Sorting and display options for the task list
    
    Attributes:
        sort_by_priority (bool):
        sort_by (SortBy): Sort option
        tags (set[Tag]): Tags that tasks in the list should have
    """
    sort_by_priority: bool
    sort_by: SortBy
    tags: Iterable[Tag]


class PlanzerCore:
    """ 
    Main core class. It contains the 
    implementation of all logical components
    """
    
    def __init__(self) -> None:
        pass

    def get_task_list(self, filter: TaskListDisplayOptions) -> tuple[Task, ...]:
        """
        Takes a dataclass and returns a tuple with tasks 
        in the correct order

        Args:
            filter (TaskListDisplayOption): List sorting and display options

        Returns:
            tuple[Task, ...]: Tuple with tasks in the correct order
        """
        if type(filter) != TaskListDisplayOptions:
            raise TypeError()

    def add_task(self, task: Task) -> None:
        """Accepts an instance of a new task and adds it to the list

        Args:
            task (Task): instance of a new task
        """
        if type(task) != Task:
            raise TypeError()

    def get_timeline(self, day: date) -> Timeline:
        """
        Returns the timeline for the specified day

        Args:
            day (date)

        Returns:
            Timeline: timeline for the specified day
        """
        if type(day) != date:
            raise TypeError()

    def task_to_event(self, task: Task, options: StartEnd | StartDuration | EndDuration) -> Event:
        """Adds a task to the timeline with the specified 
        parameters (time and either duration or end time)

        Args:
            task (Task): The task from which the event will be created
            options (CreateEventOptions): Values by which the event will be created

        Returns:
            Event: Created event
        """
        if type(task) != Task:
            raise TypeError()
        if type(options) != StartEnd and StartDuration and EndDuration:
            raise TypeError()
        
        return Event(task, options)
