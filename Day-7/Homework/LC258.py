class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return num
        if not(num%9):
            return 9
        else:
            return num%9