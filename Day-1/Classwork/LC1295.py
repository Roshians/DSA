class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            if not(len(str(i))%2):
                a+=1
        return a
