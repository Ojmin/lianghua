# from sympy import *
# import pandas as pd
#
# df = pd.read_excel("data_hs300/my_statsmodel.xlsx", sheet_name="历史行情1")
# df = df.dropna(axis=0, how="any")
# df.columns = ["date", "y", "x1", "x2", "x3", "x4", "x5"]
# a1 = Symbol("a1")
# a2 = Symbol("a2")
# a3 = Symbol("a3")
# a4 = Symbol("a4")
# a5 = Symbol("a5")
# left = []
# left.append(a1 + a2 + a3 + a4 + a5 - 1)
# for _, row in df.iterrows():
#     left.append(a1 * row.x1 + a2 * row.x2 + a3 * row.x3 + a4 * row.x4 + a5 * row.x5 - row.y)
# print(solve(left,[a1,a2,a3,a4,a5]))
from scipy import optimize
import pandas as pd
import numpy as np
from scipy.linalg import solve

df = pd.read_excel("data_hs300/my_statsmodel.xlsx", sheet_name="历史行情1")
df = df.dropna(axis=0, how="any")
df.columns = ["date", "y", "x1", "x2", "x3", "x4", "x5"]
left = [[1, 1, 1, 1, 1]]
right = [1]
for _, row in df.iterrows():
    left.append([row.x1, row.x2, row.x3, row.x4, row.x5])
    right.append(row.y)
a = np.array(left)
b = np.array(right)
print(left)
print(right)
x = solve(a, b)
print(x)
