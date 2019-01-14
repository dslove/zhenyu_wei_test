"""
The ranger thread implementation.
"""

from threading import Thread, Event
from datetime import datetime, timedelta
import time


class Ranger(Thread):

    def __init__(self, dict_cache, max_size, creation_time, timeout):
        Thread.__init__(self)
        self.dict_cache = dict_cache
        self.max_size = max_size
        self.last_clear_time = creation_time
        self.timeout = timeout
        self.stop_event = Event()

    def execute(self):
        """
        The execution body of this thread. It does two things periodically:
        1. check if the cache is going to overflow (if yes, truncate it)
        2. check if the cache is expired (if yes, clear it)
        """
        while not self._is_stopped_():
            time.sleep(2)  # patrol every 2 seconds
            if len(self.dict_cache) > self.max_size:
                self._truncate_()
            if self._is_expired_():
                self._clear_()

    # TODO: Rewrite this function during optimization, like to only delete oldest data
    def _truncate_(self):
        """
        Ideally, it will randomly delete a portion of data in cache, like 20%.
        But for now, we just simply clear the cache.
        """
        self.dict_cache.clear()
        self.last_clear_time = datetime.now()

    def _is_expired_(self):
        """
        Check if the cache is expired or not
        :return: True if the cache is expired; False if not
        """
        current_time = datetime.now()
        if current_time >= self.last_clear_time + timedelta(seconds=self.timeout):
            return True
        return False

    def _clear_(self):
        self.dict_cache.clear()
        self.last_clear_time = datetime.now()

    def stop(self):
        self.stop_event.set()

    def _is_stopped_(self):
        return self.stop_event.is_set()

    def run(self):
        self.execute()
