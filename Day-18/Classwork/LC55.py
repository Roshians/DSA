class Solution:
    def canJump(self, nums: List[int]) -> bool:
        temp = 0
        leng = len(nums)-1
        for i in range(len(nums)):
            if i > temp:
                return False
            temp = max(i + nums[i], temp)
            if temp >= leng:
                return True
        return True
