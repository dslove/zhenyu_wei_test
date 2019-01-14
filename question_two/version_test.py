"""
The test cases of the version library.
"""

from question_two import version

print(version.__doc__)
print('Version {}'.format(version.__version__))
print(version.compare.__doc__)

print('Test Cases:')
print('With wrong inputs - ')
print(version.compare())
print(version.compare(v2='1.6'))
print(version.compare(v1='1.y', v2='1.6'))
print(version.compare(v1='1.2', v2='x.6'))
print('With valid inputs - ')
print(version.compare(v1='2.6', v2='1.6'))
print(version.compare(v1='1.6', v2='2.6'))
print(version.compare(v1='1.2', v2='1.6'))
print(version.compare(v1='1.6', v2='1.2'))
print(version.compare(v1='2.4', v2='2.4'))
