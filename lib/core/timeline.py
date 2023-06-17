from dataclasses import dataclass
from datetime import time
from event import Event


@dataclass
class Timeline:
    """
    @dataclass with information about timeline

    Attributes:
        events (set[Event]): Events on timeline
        day_start_time (time): The time when the day starts. 
                               For example, it may start when the dream ends.        
        day_end_time (time): The time when the day end. 
                             Like when the dream starts.
    """

    events: set[Event]
    day_start_time: time
    dat_end_time: time
