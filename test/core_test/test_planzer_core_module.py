from lib.core import PlanzerCore

import pytest


planzer_core = PlanzerCore()


def setup_function():
    global planzer_core

    planzer_core = PlanzerCore()


@pytest.mark.parametrize(("filter"), ([1, 2, 3],
                                      "123", 123))
def test_get_task_list_with_type_error(filter):
    with pytest.raises(TypeError):
        planzer_core.get_task_list(filter)

def test_add_task_with_type_error():
    pass

def test_get_timeline_with_type_error():
    pass

def test_task_to_event_with_type_error():
    pass


def test_get_task_list_with_value_error():
    pass

def test_add_task_with_value_error():
    pass

def test_get_timeline_with_value_error():
    pass

def test_task_to_event_with_value_error():
    pass
