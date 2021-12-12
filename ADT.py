import numpy as np 

class ADT:
    def __init__(self):
        self.heap = []
    def insert(self, x):
        self.heap.append(x)
        idx = len(self.heap)
        while True:
            if idx == 1:
                return True
            elif self.heap[idx // 2 - 1] < self.heap[idx-1]:
                self.heap[idx // 2 - 1], self.heap[idx-1] = self.heap[idx-1], self.heap[idx // 2 - 1]
                idx = idx // 2
            else:
                return True

    def delete(self):
        if len(self.heap) == 0:
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        del_v = self.heap.pop()
        idx = 1
        while idx*2 <= len(self.heap):
            if idx*2 + 1 <= len(self.heap) and self.heap[idx*2] > self.heap[idx*2-1]:
                large_child_idx = idx*2 + 1
            else:
                large_child_idx = idx*2
            if self.heap[idx-1] < self.heap[large_child_idx-1]:
                self.heap[idx-1], self.heap[large_child_idx-1] = self.heap[large_child_idx-1], self.heap[idx-1]
                idx = large_child_idx
            else:
                break
        return del_v

    def create(self, arr):
        for each in arr:
            self.insert(each)
        return

    def empty(self):
        res = True if len(self.heap) == 0 else False
        return res

if __name__ == '__main__':
    # sample = np.random.randint(0, 100, size=10)
    sample = [80, 48, 90, 41, 74]
    print("sample: ")
    print(sample)
    adt = ADT()
    adt.create(sample)
    print("ADT:")
    print(adt.heap)
    print("heap sort:")
    while adt.empty() is False:
        print(adt.delete(),end=' ')