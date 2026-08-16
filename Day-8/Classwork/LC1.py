class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        index = 0

        for i in nums:
            res = target - i
            if res in dic:
                return [dic[res], index]
            else:
                dic[i] = index
                index += 1
        return []