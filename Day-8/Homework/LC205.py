class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s = {}
        mapping_t = {}
        for a, b in zip(s, t):
            if (a in mapping_s and mapping_s[a] != b) or (b in mapping_t and mapping_t[b] != a):
                return False
            mapping_s[a] = b
            mapping_t[b] = a
        return True
