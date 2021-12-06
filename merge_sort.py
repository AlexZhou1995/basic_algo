#encoding=utf-8
import numpy as np

def merger(arr1, arr2):
    res = []
    L1, L2 = len(arr1), len(arr2)
    i, j = 0, 0
    while i < L1 and j < L2:
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    if i==L1:
        res.extend(arr2[j:])
    else:
        res.extend(arr1[i:])
    return res

def merge_sort(arr):
    L = len(arr)
    if L == 1:
        return arr
    mid = L // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    res = merger(left, right)
    return res

if __name__ == '__main__':
    sample = np.random.randint(0, 1000, 10)
    print('input:')
    print(sample)
    print('answer:')
    print(np.sort(sample))
    sample = merge_sort(sample)
    print('result:')
    print(sample)
