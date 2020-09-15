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


mult()
