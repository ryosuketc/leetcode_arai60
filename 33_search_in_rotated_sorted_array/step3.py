    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            # past cliff
            if nums[middle] <= nums[-1]:
                # right of middle is sorted
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            # before cliff
            else:
                # left of middle is sorted
                if nums[left]<= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
        return -1
