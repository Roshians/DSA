class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_pos(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def last_pos(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        first = first_pos(0, len(nums) - 1)
        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        last = last_pos(first, len(nums) - 1)
        return [first, last]
