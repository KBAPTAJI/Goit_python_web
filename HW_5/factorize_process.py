from multiprocessing import Process
import sys
from time import time


def factorize(number):
    my_list = []
    result_list = []
    for el in range(1, number+1):
        result = number % el
        if result == 0:
            my_list.append(el)
        else:
            pass
    result_list.append(my_list)
    return my_list
    sys.exit(0)
    raise NotImplementedError()


if __name__ == '__main__':
    p1 = Process(target=factorize, args=(10651060,))
    p2 = Process(target=factorize, args=(10651060,))
    p3 = Process(target=factorize, args=(10651060,))
    p4 = Process(target=factorize, args=(10651060,))
    start = time()
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    print(p1.pid)
    print(p2.pid)
    print(p3.pid)
    print(p4.pid)
    print(p1.exitcode, p2.exitcode, p3.exitcode, p4.exitcode)  # None, None
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    end = time()
    print(end - start)
    print(p1.exitcode, p2.exitcode, p3.exitcode, p4.exitcode)  # 0,0,0,0
    print(p1, p2, p3, p4, sep=';')
