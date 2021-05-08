import random
import time

num_elements = 10000

S = [random.randint(0,1000000) for x in range(num_elements)]


def bubble_sort(array):
    '''Bubble Sort Algorithm. Takes an unsorted list as input and returns a sorted list'''
    k = len(array)
    S = array
    while k>0:
        for i in range(k-1):
            if S[i] > S[i+1]:
                temp = S[i]
                S[i] = S[i+1]
                S[i+1] = temp
        k -= 1
    return S

s0 = time.time()
sorted_array = bubble_sort(S)
print(time.time()-s0)
sorted_array


def merge(left, right):
    """A function to reassemble the array"""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(array):
    """A function that will be called recursively."""

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    return merge(left, right)

S = [random.randint(0,1000000) for x in range(num_elements)]

s0 = time.time()
sorted_array = merge_sort(S)
print(time.time()-s0)