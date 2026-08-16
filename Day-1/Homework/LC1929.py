class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        for i in range(leng):
            nums.insert(leng+i, nums[i])
        return nums