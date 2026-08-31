class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = [0] * 26
        window = [0] * 26

        for ch in s1:
            target[ord(ch) - 97] += 1

        for i in range(len(s2)):
            window[ord(s2[i]) - 97] += 1
            if i >= len(s1):
                window[ord(s2[i - len(s1)]) - 97] -= 1
            if window == target:
                return True

        return False
