"""
The library to provide common functions of version related, like to compare two versions.
Written in Python 3.6
"""

__version__ = 0.1


def compare(v1="", v2=""):
    """
    .compare(v1, v2)
    The method to check two versions whether one is greater than, equal to, or less than the other
    :param v1: String - the first version to compare, like '1.2'
    :param v2: String - the second version to compare
    :return: A string indicating the comparison result
    """
    if any([v1 == "", v2 == ""]):
        return 'One or both versions are not provided.'

    list1 = list(v1)
    list2 = list(v2)

    def check(a_list):
        if a_list[0].isdigit() and a_list[2].isdigit():
            return True
        return False

    if not check(list1):
        return 'Invalid input - {}'.format(v1)
    if not check(list2):
        return 'Invalid input - {}'.format(v2)

    if list1[0] > list2[0]:
        return 'Version {0} is greater than Version {1}'.format(v1, v2)
    elif list1[0] < list2[0]:
        return 'Version {0} is smaller than Version {1}'.format(v1, v2)
    else:
        if list1[2] > list2[2]:
            return 'Version {0} is greater than Version {1}'.format(v1, v2)
        elif list1[2] < list2[2]:
            return 'Version {0} is smaller than Version {1}'.format(v1, v2)
        else:
            return 'Version {0} is equal to Version {1}'.format(v1, v2)
