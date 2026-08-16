class Solution:
    def climbStairs(self, n: int) -> int:
        arr = {}
        
        def help(n):
            if n<=2:
                return n
            if n in arr:
                return arr[n]
            temp = help(n-1) + help(n-2)
            arr[n] = temp
            return temp
        return help(n)
