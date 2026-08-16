class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)-1):

            if i>0 and nums[i] == nums[i-1]:
                continue

            j = i+1
            k = len(nums) - 1

            while (j < k):
                sum = nums[i] + nums [j] + nums[k]
                if sum == 0:
                    result.append([nums[i] + nums [j] + nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                            j += 1