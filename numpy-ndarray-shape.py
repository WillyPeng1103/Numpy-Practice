import numpy as np

# 觀察資料的形狀
data = np.ones(10)  # [1, 1, 1, 1, 1, 1, 1, 1, 1]
# print(data)
data = np.array([
    [3, 1, 5],
    [1, 2, 3]
])
print(data.shape)


# 資料轉置
data = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(data.shape)
print(data)
print(data.T.shape)
print(data.T)

# 扁平化資料
data = np.array([
    [
        [2, 1, 3], [1, 3, 4]
    ], [
        [2, 3, 5], [1, 3, 5]
    ]
])   # 2x2x3

print(data.shape)
new_data = data.ravel()
print(new_data)
print(new_data.shape)

# 重塑資料的形狀
data = np.array([
    [
        [2, 1, 3], [1, 3, 4]
    ], [
        [2, 3, 5], [1, 3, 5]
    ]
])   # 2x2x3

# print(data)
# a = data.reshape(3, 4)
# print(a)
# print(a.shape)
# a = data.reshape(12)
# print(a)
# a = data.reshape(1, 4, 3)
# print(a)
# print(a.shape)

# data = np.zeros(18)
# print(data)
# data = np.zeros(18).reshape(3,6)
# print(data)
# data = np.zeros(18).reshape(2,3,3)
# print(data)

data = np.arange(9).reshape(3, 3)
print(data)
print(data.T)
