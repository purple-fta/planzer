from lib.core import *

import datetime
import pytest


@pytest.mark.parametrize("options", (1, "1", [1, 2]))
def test_create_EventOptions_with_type_error(options):
    with pytest.raises(TypeError):
        EventOptions(options)

@pytest.mark.parametrize(("task", "options"), ((1,    EventOptions(StartEnd(datetime.datetime(2020, 5, 10, 5, 10, 0), datetime.datetime(2020, 6, 10, 5, 10, 0)))),
                                               ("1",  EventOptions(StartEnd(datetime.datetime(2020, 5, 10, 5, 10, 0), datetime.datetime(2020, 6, 10, 5, 10, 0)))),
                                               (Task, EventOptions(StartEnd(datetime.datetime(2020, 5, 10, 5, 10, 0), datetime.datetime(2020, 6, 10, 5, 10, 0))))))
def test_create_Event_with_type_error(task, options):
    with pytest.raises(TypeError):
        Event(task, options)


@pytest.mark.parametrize("options", (StartEnd(datetime.datetime(2022, 5, 10),
                                              datetime.datetime(2020, 5, 10))))
def test_create_EventOptions_with_value_error(options):
    with pytest.raises(ValueError):
        EventOptions(options)

@pytest.mark.parametrize(("task", "options"), (Task("1", Priority.high, [], 0, datetime.datetime(2023, 10, 5)), EndDuration(datetime.datetime(2024, 11, 6), datetime.timedelta(10))))
def test_create_Event_with_value_error(task, options):
    pass
