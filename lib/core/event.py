from typing import NamedTuple
from task import Task
import datetime



# TODO: DOCSTRING
class StartEnd(NamedTuple):
    event_start_time: datetime.datetime
    event_end_time: datetime.datetime

class StartDuration(NamedTuple):
    event_start_time: datetime.datetime
    event_duration_time: datetime.timedelta

class EndDuration(NamedTuple):
    event_end_time: datetime.datetime
    event_duration_time: datetime.timedelta


class EventOptions:
    # TODO: DOCSTRING
    def __init__(self, options: StartEnd | StartDuration | EndDuration) -> None:
        if type(options) == StartEnd:
            self.event_start_time = options.event_start_time
            self.event_end_time = options.event_end_time
            self.event_duration_time = self.event_end_time - self.event_start_time
        if type(options) == StartDuration:
            self.event_start_time = options.event_start_time
            self.event_duration_time = options.event_duration_time
            self.event_end_time = self.event_start_time + self.event_duration_time
        if type(options) == EndDuration:
            self.event_end_time = options.event_end_time
            self.event_duration_time = options.event_duration_time
            self.event_start_time = self.event_end_time - self.event_duration_time


    def get_event_duration(self) -> datetime.timedelta:
        pass


class Event(EventOptions):
    # TODO: DOCSTRING
    def __init__(self, task: Task, options: StartEnd | StartDuration | EndDuration) -> None:
        super().__init__(options)
