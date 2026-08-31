class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            used = 1
            current = 0
            for w in weights:
                if current + w > mid:
                    used += 1
                    current = 0
                current += w
            if used <= days:
                right = mid
            else:
                left = mid + 1
        return left
