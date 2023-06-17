from dataclasses import dataclass
from datetime import date
from enum import Enum

from event import Event, CreateEventOptions
from timeline import Timeline
from task import Task

class SortedBy(Enum):
    priority = 0
    closest_to_deadline = 1


@dataclass
class TaskListDisplayOption: #TODO: ДОРОБИТИ
    pass


class PlanzerCore:
    """ 
    Main core class. It contains the 
    implementation of all logical components
    """
    
    def __init__(self) -> None:
        pass

    def get_task_list(self, filter: TaskListDisplayOption) -> tuple[Task, ...]:
        """
        Takes a dataclass and returns a tuple with tasks 
        in the correct order

        Args:
            filter (TaskListDisplayOption): List sorting and display options

        Returns:
            tuple[Task, ...]: Tuple with tasks in the correct order
        """
        pass

    def add_task(self, task: Task) -> None:
        """Accepts an instance of a new task and adds it to the list

        Args:
            task (Task): instance of a new task
        """
        pass

    def get_timeline(self, day: date) -> Timeline:
        """
        Returns the timeline for the specified day

        Args:
            day (date)

        Returns:
            Timeline: timeline for the specified day
        """
        pass

    def task_to_event(self, task: Task, options: CreateEventOptions) -> Event:
        """Adds a task to the timeline with the specified 
        parameters (time and either duration or end time)

        Args:
            task (Task): The task from which the event will be created
            options (CreateEventOptions): Values by which the event will be created

        Returns:
            Event: Created event
        """
        pass
