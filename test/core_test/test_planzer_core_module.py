from lib.core import *

import pytest


planzer_core = PlanzerCore()


def setup_function():
    global planzer_core

    planzer_core = PlanzerCore()


@pytest.mark.parametrize("filter", ([1, 2, 3],
                                      "123", 123))
def test_get_task_list_with_type_error(filter):
    print(filter)
    with pytest.raises(TypeError):
        planzer_core.get_task_list(filter)

@pytest.mark.parametrize(("task"), ([1, 2, 3],
                                    "123", 123))
def test_add_task_with_type_error(task):
    with pytest.raises(TypeError):
        planzer_core.add_task(task)

@pytest.mark.parametrize(("day"), ([1, 2, 3],
                                   "123", 123))
def test_get_timeline_with_type_error(day):
    with pytest.raises(TypeError):
        planzer_core.get_timeline(day)

@pytest.mark.parametrize(("task", "options"), ( [1123, "123"],
                                                ["12", [1, 2, 3]],
                                                ["12", [1, "1", 3]] ))
def test_task_to_event_with_type_error(task, options):
    with pytest.raises(TypeError):
        planzer_core.task_to_event(task, options)

@pytest.mark.parametrize(("filter"), (1, "123", 123))
def test_create_TaskListDisplayOptions_with_type_error(filter):
    with pytest.raises(TypeError):
        TaskListDisplayOptions(filter)


@pytest.mark.parametrize(("filter"), ([1, 2, 3],
                                      "123", 123))
def test_get_task_list_with_value_error(filter):
    with pytest.raises(TypeError):
        planzer_core.get_task_list(filter)

@pytest.mark.parametrize(("task"), ([1, 2, 3],
                                    "123", 123))
def test_add_task_with_value_error(task):
    with pytest.raises(TypeError):
        planzer_core.add_task(task)

@pytest.mark.parametrize(("day"), ([1, 2, 3],
                                   "123", 123))
def test_get_timeline_with_value_error(day):
    with pytest.raises(TypeError):
        planzer_core.get_timeline(day)

@pytest.mark.parametrize(("task", "options"), ( [1123, "123"],
                                                ["12", [1, 2, 3]],
                                                ["12", [1, "1", 3]] ))
def test_task_to_event_with_value_error(task, options):
    with pytest.raises(TypeError):
        planzer_core.task_to_event(task, options)

@pytest.mark.parametrize(("tags"), ([1, Tag("tag", (0, 150, 150))],
                                    (Tag("tag", (0, 150, 150)), Tag),
                                    [1, Tag, 5]))
def test_create_TaskListDisplayOptions_with_value_error(tags):
    with pytest.raises(ValueError):
        TaskListDisplayOptions(tags)
