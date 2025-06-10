# WA
class Solution1:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # mid は崖登りの途中 -> 最小値は mid より右にあるはずで、mid 自体は最小にならない
            if nums[0] < nums[mid]:
                left = mid + 1
            # mid は崖を降りた後 -> 最小値は mid またはその左にあるはず (崖を降りた直後の可能性があるので、mid 自体も最小になるかもしれない)
            else:
                right = mid
        return nums[left] # == right

# WA (rotate されていなかったときの処理)
class Solution2:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # mid は崖登りの途中 -> 最小値は mid より右にあるはずで、mid 自体は最小にならない
            if nums[0] < nums[mid]:
                left = mid + 1
            # mid は崖を降りた後 -> 最小値は mid またはその左にあるはず (崖を降りた直後の可能性があるので、mid 自体も最小になるかもしれない)
            else:
                right = mid
        return nums[left] # == right

# AC (`if nums[0] <= nums[mid]:` 等号を含める形に変更。mid = 0 になったときに処理できない)
class Solution3:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # mid は崖登りの途中 -> 最小値は mid より右にあるはずで、mid 自体は最小にならない
            if nums[0] <= nums[mid]:
                left = mid + 1
            # mid は崖を降りた後 -> 最小値は mid またはその左にあるはず (崖を降りた直後の可能性があるので、mid 自体も最小になるかもしれない)
            else:
                right = mid
        return nums[left] # == right

 # nums[-1] との比較。
 class Solution4:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # mid は崖を降りた後 -> 最小値は mid またはその左にあるはず (崖を降りた直後の可能性があるので、mid 自体も最小になるかもしれない)
            if nums[mid] <= nums[-1]:
                right = mid
            # mid は崖登りの途中 -> 最小値は mid より右にあるはずで、mid 自体は最小にならない
            else:
                left = mid + 1
        return nums[left] # == right
