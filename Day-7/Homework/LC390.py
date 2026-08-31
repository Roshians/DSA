class Solution:
    def lastRemaining(self, n: int) -> int:
        left = True
        remaining = n
        step = 1
        start = 1

        while remaining > 1:
            if left or remaining % 2 == 1:
                start += step
            left = not left
            remaining //= 2
            step *= 2

        return start
