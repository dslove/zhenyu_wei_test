"""
The test cases of the cache library.
"""

from question_three import cache
import time

# Test Cases:

print('\nTest Case 1-------------------------------')

# Test Case 1: use cache
the_cache = cache.GDLRUCache(10, 5)
# Query data not in a new cache but in database
# None of these entries is in cache
print(the_cache.get('date'))
print(the_cache.get('candidate'))
print(the_cache.get('interviewer'))
# Query data in cache
# Now they are all in cache
print(the_cache.get('date'))
print(the_cache.get('candidate'))
print(the_cache.get('interviewer'))
# Query data neither in cache nor in database
print(the_cache.get('result'))
print('Shutting down cache...')

the_cache.shut_down()  # shut down the cache

print('\nTest Case 2-------------------------------')

# Test Case 2: handle cache expiration
the_cache = cache.GDLRUCache(10, 5)  # set expiration to 5 seconds
print(the_cache.get('date'))  # query a data that is not in cache yet
print(the_cache.get('date'))  # query it again, and now it should be in cache
for i in range(6):  # wait for 6 seconds for cache expiration
    print(6-i)
    time.sleep(1)
print(the_cache.get('date'))  # cache should be cleared and the data should not be in cache again
print('Shutting down cache...')
the_cache.shut_down()  # shut down the cache

print('\nTest Case 3-------------------------------')

# Test Case 3: handle cache overflow
the_cache = cache.GDLRUCache(10, 5)  # set max_size to 10 entries
print(the_cache.get('date'))  # query a data that is not in cache yet
print(the_cache.get('date'))  # query it again, and now it should be in cache which has only 1 entry
for i in range(10):  # flush the cache with 10 entries
    print('Inserting data entry - {}'.format(i+1))
    the_cache.set(str(i), 'test data')  # in production this API is private
time.sleep(3)  # wait for the ranger to notice that the cache is full
print(the_cache.get('date'))  # cache should be cleared and the data should not be in cache again
print('Shutting down cache...')
the_cache.shut_down()  # shut down the cache
