# 15.1.2 프로세스 생성하기(2): multiprocessing

import multiprocessing
import os
def whoami(what):
    print("Process %s says: %s" % (os.getpid(), what))

if __name__ == "__main__":
    whoami("I'm the main program")

    for n in range(4):
        p = multiprocessing.Process(target=whoami,
                                    args=("I'm function %s" % n,))
        p.start()
