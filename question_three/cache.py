"""
The library to provide cache functionality.
Written in Python 3.6
"""

from question_three import ranger
import datetime
import time

__version__ = 0.1


class GDLRUCache:

    def __init__(self, max_size, timeout):
        self.dict_cache = {}
        self.max_size = max_size
        self.creation_time = datetime.datetime.now()
        self.timeout = timeout
        self.ranger = ranger.Ranger(self.dict_cache, self.max_size, self.creation_time, self.timeout)
        self.ranger.start()  # start the ranger thread to monitor the cache
        self.fake_db = {}
        self._mock_db_()

    def _mock_db_(self):
        """
        Since it is not able to really implement a DBMS driver and connect to a real DB,
        here we just fake a DB with an in-memory dictionary as a test stub.
        """
        self.fake_db['date'] = '2019/01/14'
        self.fake_db['candidate'] = 'Zhenyu Wei'
        self.fake_db['interviewer'] = 'Ormuco'

    def get(self, query):
        """
        Get the result for a query from the cache
        :param query: The query
        :return: The result
        """
        result = self.dict_cache.get(query, None)
        if result is not None:
            print('Data is found in cache.')
        else:  # if a query is not found in cache, look up in DB and save it to cache
            print('Data is not available in cache. Querying DB...')
            result = self._query_db_(query)
            self.set(query, result)
        return result

    # TODO: Rewrite this function when a real DB connectivity is available
    def _query_db_(self, query):
        """
        Ideally, it will query a database when a query is not found in cache.
        But for now, we just simply query the fake database.
        :param query: The query request
        :return: The query result
        """
        return self.fake_db.get(query, 'Data not available in Database too!')  # return a result anyway

    def set(self, query, result):
        """
        Store a new query: result pair in the cache
        :param query: The query
        :param result: The result
        """
        self.dict_cache[query] = result
        """
        The idea here is to notify other caches, when a new data entry is added in local cache.
        Every distributed cache should do the same thing so that they all have consistent data.
        And in this way, even though there is a system or network crash, the cache can be restored quickly.
        """
        self._broadcast_(query, result)

    # TODO: Implement this function when RESTFul API is available
    def _broadcast_(self, query, result):
        """
        Broadcast this new entry to peer caches on the Internet
        Ideally, there will be a set of supporting web services underneath
        """
        pass

    def add(self, query, result):
        """
        Handle obtained broadcasts.
        :param query: The query
        :param result: The result
        """
        if query not in self.dict_cache:
            self.dict_cache[query] = result

    def shut_down(self):
        """
        Shut down the cache and also close its ranger thread
        """
        self.ranger.stop()
        time.sleep(5)  # wait for 5 seconds for the ranger thread to stop
