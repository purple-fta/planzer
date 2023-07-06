from lib.core import *

import datetime
import pytest


@pytest.mark.parametrize("options", (1, "1", [1, 2]))
def test_create_EventOptions_with_type_error(options):
    with pytest.raises(TypeError):
        EventOptions(options)

@pytest.mark.parametrize(("task", "options"), ((1,    EventOptions(StartEnd(datetime.datetime(2020, 5, 10, 5, 10, 0), datetime.datetime(2020, 6, 10, 5, 10, 0)))),
                                               (Task("123", Priority.high, [], 0, datetime.datetime(2000, 10, 10)),  0),
                                               (Task, EventOptions(StartEnd(datetime.datetime(2020, 5, 10, 5, 10, 0), datetime.datetime(2020, 6, 10, 5, 10, 0))))))
def test_create_Event_with_type_error(task, options):
    with pytest.raises(TypeError):
        Event(task, options)


@pytest.mark.parametrize("options", (StartEnd(datetime.datetime(2022, 5, 10),
                                              datetime.datetime(2020, 5, 10))))
def test_create_EventOptions_with_value_error(options):
    with pytest.raises(ValueError):
        EventOptions(options)

def test_create_Event_with_value_error():
    with pytest.raises(ValueError):
        Event(Task("1", Priority.high, [], 0, datetime.datetime(2023, 10, 5)), EndDuration(datetime.datetime(2024, 11, 6), datetime.timedelta(10)))


def test_get_event_duration():
    event_options = EventOptions(StartEnd(datetime.datetime(2020, 5, 10), datetime.datetime(2021, 5, 11, 8, 21)))
    assert event_options.get_event_duration() == datetime.timedelta(days=366, seconds=30060)
