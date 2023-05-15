# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import pickle

import numpy as np
from scipy.linalg import lstsq

a = np.array([[1, 2, 3, 4], [4, 9, 16, 1], [27, 64, 1, 8]])
b = np.array([1, 1, 1])
res = lstsq(a, b)
print(res)
