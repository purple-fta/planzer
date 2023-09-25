from dataclasses import dataclass
from typing import Set, Iterable, List
from datetime import date, time, datetime
from enum import Enum


from .event import Event, EventOptions, StartEnd, StartDuration, EndDuration
from .timeline import Timeline
from .task import Task, Priority
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
    tags: Iterable[Tag] #TODO


class PlanzerCore:
    """ 
    Main core class. It contains the 
    implementation of all logical components
    """
    
    def __init__(self) -> None:
        self.tasks: List[Task] = []
        self.events: List[Event] = []

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
        
        result_tasks = []

        if filter.sort_by_priority:
            high_priority_tasks = []
            normal_priority_tasks = []
            low_priority_tasks = []

            for task in self.tasks:
                if task.priority == Priority.high:
                    high_priority_tasks.append(task)
                elif task.priority == Priority.normal:
                    normal_priority_tasks.append(task)
                elif task.priority == Priority.low:
                    low_priority_tasks.append(task)

            if filter.sort_by == SortBy.closest_to_deadline:
                datetime_now = datetime.now()
                
                high_priority_tasks.sort(key=lambda task: datetime_now - task.deadline)
                normal_priority_tasks.sort(key=lambda task: datetime_now - task.deadline)
                low_priority_tasks.sort(key=lambda task: datetime_now - task.deadline)

                result_tasks = high_priority_tasks + normal_priority_tasks + low_priority_tasks
        else:
            pass

        return tuple(result_tasks)


    def add_task(self, task: Task) -> None:
        """Accepts an instance of a new task and adds it to the list

        Args:
            task (Task): instance of a new task
        
        Raises:
            ValueError: If task with same name already exists
        """
        if type(task) != Task:
            raise TypeError()
        
        tasks_name = [t.name for t in self.tasks]
        if task.name not in tasks_name:
            self.tasks.append(task)
        else:
            raise ValueError("A task with the same name already exists")


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
        
        events_in_day = []

        for event in self.events:
            if event.event_start_time.date() == day:
                events_in_day.append(event)

        # TODO: Timeline argument from Set to Iterable
        result_timeline = Timeline(set(events_in_day), time.min, time.max)

        return result_timeline


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

        event = Event(task, options)

        self.events.append(event)

        return event
