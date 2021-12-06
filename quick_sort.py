#encoding=utf-8
import numpy as np

def quick_sort(arr, lo, hi):
    if lo < hi: # 不要忘记这里
        m = arr[lo]
        i, j = lo, hi
        while i < j:
            while i < j and arr[i] < m:
                i += 1
            arr[j] = arr[i]
            while i < j and arr[j] >= m:  #注意这里：1.不要忘了i<j的条件。2.记得有一个要有等于号
                j -= 1
            arr[i] = arr[j]
        arr[i] = m
        quick_sort(arr, lo, i-1)
        quick_sort(arr, i+1, hi)

if __name__ == '__main__':
    sample = np.random.randint(0, 1000, 10)
    print(sample)
    quick_sort(sample, 0, len(sample)-1)
    print(sample)