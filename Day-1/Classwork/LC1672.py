class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        highest = 0

        for i in accounts:
            sum = 0
            for j in i:
                sum += j
            if highest<sum:
                highest = sum
        return highest
