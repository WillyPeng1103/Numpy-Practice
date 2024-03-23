import numpy as np

# data = np.array([1, 5, 2, 10])
# print(data[2])

# # 多維度資料
# data = np.array([
#     [0, 1],
#     [10, -2],
#     [5, 8]
# ])
# print(data[0, 1])  # 1
# print(data[1, 0])  # 10
# print(data[2, 0])  # 5

# # 單維度的切片 Slicing
# data = np.array([-1, -5, 2, 3])
# print(data[0:3]) # [-1, -5, 2]
# print(data[:2])  # [-1, -5]
# print(data[2:])  # [2, 3]
# print(data[:])   # [-1, -5, 2, 3]

# # 多維度的資料
# data = np.array([
#     [0, 1, 2], [3, 4, 5],
#     [5, 4, 2], [2, 1, 0]
# ])
# print(data[1:3, 0:2])  # [[3,4], [5,4]]
# print(data[0:2, 1])   #[1, 4]

# 使用 ... 代表全部
data = np.array([
    [
        [8, 1, 3], [-5, 5, 2]
    ], [
        [0, 1, 6], [4, 4, -3]
    ]
])
print(data[0, ...])  # [[ 8 , 1 , 3], [-5 , 5 , 2]]
print(data[..., 1:3])  # [[[1,3], [5,2]],[[1,6], [4, -3]]]
