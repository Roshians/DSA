class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        def bk(start):
            ans.append(curr[:])

            for i in range(start, len(nums)):
                curr.append(nums[i])
                bk(i+1)
                curr.pop()

        bk(0)
        return ans