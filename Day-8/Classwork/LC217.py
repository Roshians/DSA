class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        index = 0
        for i in nums:
            if i in dic:
                return True
            else: 
                dic[i] = index
                index += 1
        return False

            