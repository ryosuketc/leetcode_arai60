class MinHeap:
    def __init__(self):
        self.heap = []
    
    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return str(self.heap)

    def push(self, value):
        # Insert to the last elemente in the complete binary tree and sift up the last (inserted) element.
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)
    
    def peek(self):
        if not self.heap:
            raise IndexError('Heap is empty')
        return self.heap[0]
    
    def pop(self):
        if not self.heap:
            raise IndexError('Heap is empty')
        min_value = self.heap[0]
        last_value = self.heap.pop()
        if self.heap:
            self.heap[0] = last_value
            self._sift_down(0)
        return min_value
    
    def heapify(self, elements):
        self.heap =  list(elements)
        last_parent = self._parent(len(self.heap) - 1)
        for i in reversed(range(last_parent + 1)):
            self._sift_down(i)


    def _parent(self, index):
        if index == 0:
            return None
        return (index - 1) // 2

    def _left(self, index):
        left_index = 2 * index + 1
        if left_index >= len(self.heap):
            return None
        return left_index

    def _right(self, index):
        right_index = 2 * index + 2
        if right_index >= len(self.heap):
            return None
        return right_index

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _sift_up(self, index):
        parent_index = self._parent(index)
        while parent_index is not None and self.heap[index] < self.heap[parent_index]:
            self._swap(index, parent_index)
            index = parent_index
            parent_index = self._parent(parent_index)
    
    def _sift_down(self, index):
        while True:
            smallest_index = index
            left_index = self._left(index)
            right_index = self._right(index)
            if left_index is not None and self.heap[left_index] < self.heap[smallest_index]:
                smallest_index = left_index
            if right_index is not None and self.heap[right_index] < self.heap[smallest_index]:
                smallest_index = right_index
            
            if smallest_index == index:
                # sift down is finished
                break
            self._swap(index, smallest_index)
            index = smallest_index



class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.largest_nums_up_to_kth = MinHeap()
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        self.largest_nums_up_to_kth.push(val)
        if len(self.largest_nums_up_to_kth) > self.k:
            self.largest_nums_up_to_kth.pop()
        
        return self.largest_nums_up_to_kth.peek()



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
