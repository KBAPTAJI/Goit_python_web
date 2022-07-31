from random import randint
from unittest import result

result = ''

counter = 1
number = 4
number_2 = 1
for i in range(1, 121):
    result += '('
    result += str(i)
    result += ','
    result += str(randint(60, 100))
    result += ','
    if counter < number:
        counter += 1
        result += str(number_2)
        result += '),'
    elif counter == number:
        result += str(number_2)
        result += '),'
        number += 4
        number_2 += 1
        counter += 1
result2 = result[:-1]
result2 += ';'
with open('notes.txt', 'w') as file:
    file.write(result2)
