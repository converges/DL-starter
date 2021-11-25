'''
Github: https://github.com/converges/DL-starter/
Author: An
'''
''' Exercise 01: Python Programming
Define a function that returns a inner product(dot product) of two intergers: innerProduct(a, b).
'''

def innerProduct(a, b):
    result = 0

    for i in range(len(a)):
        result += a[i] * b[i]

    return result

if __name__ == '__main__':
    a = [-1, 0, 1]
    b = [1, 0, -1]

    result = innerProduct(a, b)
    print(f"{a}•{b} = {result}")
    
# Done: 2021-11-05.