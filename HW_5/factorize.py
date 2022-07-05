from time import time
from unittest import result


def factorize(number):
    my_list = []
    for el in range(1, number+1):
        result = number % el
        if result == 0:
            my_list.append(el)
        else:
            pass
    return my_list


if __name__ == '__main__':
    start = time()
    a, b, c, d = factorize(10651060), factorize(
        10651060), factorize(10651060), factorize(10651060)
    end = time()
    result = (end - start)
    print(result)
    print(a, b, c, d, sep=';')
