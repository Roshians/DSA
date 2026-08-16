class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = 0, 1
        n = len(nums)
        while even < n and odd < n:
            if not(nums[even] % 2):
                even += 2
            elif (nums[odd])%2:
                odd += 2
            else:
                nums[even], nums[odd] = nums[odd], nums[even]
                even+=2
                odd+=2
        return nums        