# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import pickle

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def np_hello():
    # x = np.arange(5)
    # print(x) # 一维数组 [0, 1, 2]
    # print(x.shape) # (3,)
    #
    #
    # x1 = x[:, np.newaxis] # 增加一个维度
    # print(x1)  # 一维数组 [0, 1, 2]
    # print(x1.shape)  # (3,1)
    #
    # x2 = x1[:, None]
    # print(x2)  # 一维数组 [0, 1, 2]
    # print(x2.shape)  # (3,1)

    x = np.array([[1, 2, 3, 4,5], [5, 6, 7, 8,5], [9, 10, 11, 12,13]])

    print(x)  # 一维数组 [0, 1, 2]
    print(x.shape)  # (3,)

    print("-------------------")

    # 取第一行数据
    y= x[:, 0]
    print(y)  # 一维数组 [0, 1, 2]
    print(y.shape)  # (3,)

    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(pickle)
    print()
    np_hello()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
