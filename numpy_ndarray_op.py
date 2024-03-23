import numpy as np

# 逐元運算
data1 = np.array([3, 2, 10])
data2 = np.array([1, 3, 6])
r = data1 + data2
print("加法", r)
r = data1 - data2
print('減法', r)
r = data1 * data2
print('乘法', r)
r = data1 / data2
print ('除法', r)
r = data1 > data2
print('是否大於',r)
r = data1 == data2
print('是否等於', r)

# 矩陣運算
data1 = np.array([  # 1x2
    [1, 4]
])
data2 = np.array([  # 2x3
    [1, 6, 3],
    [7, -1, 0]
])
r = data1.dot(data2)
r = data1@data2
print('內積', r)
r = np.outer(data1, data2)
print('外積', r)

# 統計運算
data = np.array([  # 2x3
    [2, 1, 7],
    [-5, 3, 8]
])
r = data.cumsum()  # 逐值累加
print(r)
r = data.cumsum(axis=0)
print(r)
r = data.cumsum(axis=1)
print(r)

a = data.sum(axis=0)  # 針對column作總和 (針對第一個維度)
print(a)
a = data.sum(axis=1)  # 針對row作總和  (針對第二個維度)
print(a)
a = data.mean(axis=0)
print(a)

a = data.sum()
print("總和", a)
a = data.max()
print("最大值", a)
a = data.mean()
print("平均數", a)
a = data.std()
print("標準差", a)
