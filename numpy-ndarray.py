import numpy as np


a = np.array([1, 2, 3])   # 1x3
a = np.array([   # 2x3
    [1, 2, 3],
    [4, 5, 6]
])
a = np.array([  # 2x2x3
    [
        [1, 2, 3], [3, 4, 5]
    ], [
        [6, 7, 8], [9, 10, 11]
    ]
])

# a = np.empty(3)
a = np.empty([2, 3])
a = np.empty([2, 2, 3])

a = np.zeros([3])
a = np.zeros([2, 3])
a = np.zeros([2, 3, 3])

a = np.ones([3])
a = np.ones([2, 3, 2])

a = np.arange(8)
a = np.arange(8)
