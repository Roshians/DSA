class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newL = []
        for i in range(n):
            newL.insert(2*i, nums[i])
            newL.insert(2*i+1, nums[i+n])
        return newL


            
