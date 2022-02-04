import numpy as np

class Variable:
    def __init__(self, data):
        self.data = data

if __name__ == "__main__":
    data = np.array(1.0)
    x = Variable(data)
    print(x.data)

    x.data =np.array(2.0)
    print(x.data)

    # Plus Alpha

    # a scalar
    _x = np.array(1)
    print(_x.ndim)

    # a vector
    _x = np.array([1,2,3])
    print(_x.ndim)

    # a matrix
    _x = np.array(
        [
            [1, 2, 3],
            [4, 5, 6]
            ])
    print(_x.ndim)