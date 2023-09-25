""" Module with classes for creating and managing events """

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
            self._set_start_end(options.event_start_time, options.event_end_time)
        elif type(options) == StartDuration:
            self._set_start_duration(options.event_start_time, options.event_duration_time)
        elif type(options) == EndDuration:
            self._set_duration_end(options.event_duration_time, options.event_end_time)
        else:
            raise TypeError("")  # TODO:

    def get_event_duration(self) -> datetime.timedelta:
        """
        Returns the duration of the event

        Returns:
            Duration of the event
        """

        return self.event_duration_time

    def _set_start_end(self, start: datetime.datetime, end: datetime.datetime):
        if start > end:
            raise ValueError("Start time > end time")
        self.event_start_time = start
        self.event_end_time = end
        self.event_duration_time = self.event_end_time - self.event_start_time

    def _set_start_duration(self, start: datetime.datetime, duration: datetime.timedelta):
        self.event_start_time = start
        self.event_duration_time = duration
        self.event_end_time = self.event_start_time + self.event_duration_time

    def _set_duration_end(self, duration: datetime.timedelta, end: datetime.datetime):
        self.event_end_time = end
        self.event_duration_time = duration
        self.event_start_time = self.event_end_time - self.event_duration_time

    def set_options(self, start: datetime.datetime | None, duration: datetime.timedelta | None,
                    end: datetime.datetime | None):
        """
            Calculate missing data from existing data and assign them.
            Among the arguments there must be only one None, and it will be calculated.
        """

        # TODO: Нужно проверить передаваемы данные
        if start is None:
            self._set_duration_end(duration, end)
        elif duration is None:
            self._set_start_end(start, end)
        else:
            self._set_start_duration(start, duration)


class Event(EventOptions):
    """
    Event class with time and task information
    """
    def __init__(self, task: Task, options: StartEnd | StartDuration | EndDuration) -> None:
        super().__init__(options)
        
        if type(task) != Task:
            raise TypeError("")  # TODO:
        if task.deadline < self.event_end_time:
            raise ValueError()
        if task.deadline < self.event_start_time:
            raise ValueError()
        
        self.task = task
