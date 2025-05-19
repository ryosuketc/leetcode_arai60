class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.largest_nums_up_to_kth = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.largest_nums_up_to_kth, val)
        if len(self.largest_nums_up_to_kth) > self.k:
            heapq.heappop(self.largest_nums_up_to_kth)
        return self.largest_nums_up_to_kth[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)