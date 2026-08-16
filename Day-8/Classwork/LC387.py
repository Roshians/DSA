class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in s:
            dic[i] = dic.setdefault(i, 0) + 1
        
        for i in dic.items():
            if i[1] == 1:
                return s.index(i[0])
        return -1