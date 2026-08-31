class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            prev_two = 0
            prev_one = 0
            for num in arr:
                prev_two, prev_one = prev_one, max(prev_one, prev_two + num)
            return prev_one

        return max(helper(nums[:-1]), helper(nums[1:]))
