from threading import Thread
from time import sleep


class SimpleThread(Thread):

    def run(self):
        print('Run')
        sleep(1)
        print('Done')


simple_thread = SimpleThread()
simple_thread2 = SimpleThread()
simple_thread.start()
simple_thread2.start()
print('end')
