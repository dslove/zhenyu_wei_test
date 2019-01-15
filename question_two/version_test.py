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
print('With valid inputs (x.y) - ')
print(version.compare(v1='2.6', v2='1.6'))
print(version.compare(v1='1.6', v2='2.6'))
print(version.compare(v1='1.2', v2='1.6'))
print(version.compare(v1='1.6', v2='1.2'))
print(version.compare(v1='2.4', v2='2.4'))
print('With valid inputs (x*.y*) - ')
print(version.compare(v1='1.11', v2='2.1'))
print(version.compare(v1='1.36', v2='1.28'))
print(version.compare(v1='12.10', v2='12.10'))
print(version.compare(v1='0.20', v2='0.10'))
print(version.compare(v1='12.00', v2='12.01'))
print(version.compare(v1='345.678', v2='345.001'))
