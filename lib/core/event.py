from typing import NamedTuple
from .task import Task
import datetime



class StartEnd(NamedTuple):
    """
    A class for specifying values to describe the event.
    """
    event_start_time: datetime.datetime
    event_end_time: datetime.datetime

class StartDuration(NamedTuple):
    """
    A class for specifying values to describe the event.
    """
    event_start_time: datetime.datetime
    event_duration_time: datetime.timedelta

class EndDuration(NamedTuple):
    """
    A class for specifying values to describe the event.
    """
    event_end_time: datetime.datetime
    event_duration_time: datetime.timedelta


class EventOptions:
    """
    A class with all the data to describe the location of the event on the timeline
    """
    def __init__(self, options: StartEnd | StartDuration | EndDuration) -> None:
        if type(options) == StartEnd:
            if options.event_start_time > options.event_end_time:
                raise ValueError("Start time > end time")
            self.event_start_time = options.event_start_time
            self.event_end_time = options.event_end_time
            self.event_duration_time = self.event_end_time - self.event_start_time
        elif type(options) == StartDuration:
            self.event_start_time = options.event_start_time
            self.event_duration_time = options.event_duration_time
            self.event_end_time = self.event_start_time + self.event_duration_time
        elif type(options) == EndDuration:
            self.event_end_time = options.event_end_time
            self.event_duration_time = options.event_duration_time
            self.event_start_time = self.event_end_time - self.event_duration_time
        else:
            raise TypeError("")

    def get_event_duration(self) -> datetime.timedelta:
        pass


class Event(EventOptions):
    """
    Event class with time and task information
    """
    def __init__(self, task: Task, options: StartEnd | StartDuration | EndDuration) -> None:
        super().__init__(options)
        
        if type(task) != Task:
            raise TypeError("")
        if task.deadline < self.event_end_time:
            raise ValueError()
        if task.deadline < self.event_start_time:
            raise ValueError()
