'''
Github: https://github.com/converges/DL-starter/
Author: An
'''
''' Exercise 02: Python Programming
There's an int-array 'numbers'.
Define a function 'solution' that returns a descending array of all products of two elements out of 'numbers'. 
'''

def solution(numbers):
    result = set() # Keep result from duplications.

    length = len(numbers)

    for i in range(0, length): # (i,j) is all unordered tuple of two different elements of [0~9].
        for j in range(i+1, length):
            result.add(numbers[i]*numbers[j])

    return sorted(list(result), reverse=True)

if __name__ == '__main__':
    numbers = [5, 0, 1, 2]

    result = solution(numbers)
    print(result)

# Done: 2021-11-11.