class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sum = nums[0]
        maxi = nums[0]

        for i in range(len(nums)):
            sum  = max(nums[i], nums[i] * sum)
            maxi = max(sum, maxi)
        return maxi