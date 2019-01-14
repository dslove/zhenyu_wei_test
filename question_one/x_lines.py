def is_overlap(line1, line2):
    if any([(line1[0] < line2[0] and line1[1] < line2[0]), (line1[0] > line2[1] and line1[1] > line2[1])]):
        return 'NOT Overlapped'
    return 'Overlapped'


print('Test Cases:')
x = [1, 5]
y = [6, 10]
print('Line {} and Line {} are {}'.format(x, y, is_overlap(x, y)))
x = [1, 6]
y = [6, 10]
print('Line {} and Line {} are {}'.format(x, y, is_overlap(x, y)))
x = [1, 8]
y = [6, 10]
print('Line {} and Line {} are {}'.format(x, y, is_overlap(x, y)))
x = [7, 16]
y = [6, 10]
print('Line {} and Line {} are {}'.format(x, y, is_overlap(x, y)))
x = [10, 16]
y = [6, 10]
print('Line {} and Line {} are {}'.format(x, y, is_overlap(x, y)))
x = [12, 16]
y = [6, 10]
print('Line {} and Line {} are {}'.format(x, y, is_overlap(x, y)))
x = [7, 8]
y = [6, 10]
print('Line {} and Line {} are {}'.format(x, y, is_overlap(x, y)))
x = [1, 16]
y = [6, 10]
print('Line {} and Line {} are {}'.format(x, y, is_overlap(x, y)))
