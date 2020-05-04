import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn


def fib(x, y, z, count):
    if count > 0:
        z = x + y
        x = y
        y = z
        print(z, end = " ")
        fib(x, y, z, count - 1)


x = 0
y = 1
z = 0
count = (int(input("How many iterations? ")))
print(x, y, end = " ")
fib(x, y, z, count - 2)
