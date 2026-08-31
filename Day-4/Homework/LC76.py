class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        have = {}
        required = len(need)
        formed = 0
        left = 0
        best = ""
        best_len = float('inf')

        for right, ch in enumerate(s):
            have[ch] = have.get(ch, 0) + 1
            if ch in need and have[ch] == need[ch]:
                formed += 1

            while left <= right and formed == required:
                window_len = right - left + 1
                if window_len < best_len:
                    best_len = window_len
                    best = s[left:right + 1]
                left_ch = s[left]
                if left_ch in need:
                    have[left_ch] -= 1
                    if have[left_ch] < need[left_ch]:
                        formed -= 1
                left += 1

        return best
