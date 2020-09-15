import random
import numpy as np

def array():
    a = np.array([[random.randint(0,100) for i in range(4)],[random.randint(0,100) for i in range(4)],
                  [random.randint(0,100) for i in range(4)],[random.randint(0,100) for i in range(4)]])
    print(a)
    return a

