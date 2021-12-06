import numpy as np

def stock1(arr):
    min_price = 2^30
    max_get = 0
    for each in arr:
        min_price = min(min_price, each)
        max_get = max(max_get, each - min_price)
    return max_get


if __name__ == '__main__':
    sample = [8,9,2,5,4,7,1]
    print(sample)
    result = stock1(sample)
    print(result)