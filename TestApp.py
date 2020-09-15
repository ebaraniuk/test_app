import random
import numpy as np


def array():
    a = np.array([[random.randint(0, 10) for i in range(4)], [random.randint(0, 10) for i in range(4)],
                  [random.randint(0, 10) for i in range(4)], [random.randint(0, 10) for i in range(4)]])
    return a


def mult():
    a = array()
    b = array()
    print(a, b, np.dot(a, b))


def statistic():
    s = np.array([random.randint(0, 100) for i in range(50)])
    print("List:", s)
    print("Median:", np.median(s))
    print("Max:",max(s))
    print("Average:",sum(s)/len(s))
    a = np.array([[random.randint(0, 10) for i in range(4)], [random.randint(0, 10) for i in range(4)],
                  [random.randint(0, 10) for i in range(4)]])
    print("Corrcoef:", np.corrcoef(a))


mult()
statistic()