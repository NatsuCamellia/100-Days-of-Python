from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

def download_task(filename):
    print('Download. PID=[%d].' % getpid())
    print('Downloading %s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s downloaded! %s seconds elapsed.' % (filename, time_to_download))

def main():
    start = time()
    p1 = Process(target=download_task, args=('Python从入门到住院.pdf', ))
    p1.start()
    p2 = Process(target=download_task, args=('Peking Hot.avi', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('Cost %.2f second.' % (end - start))


if __name__ == '__main__':
    main()