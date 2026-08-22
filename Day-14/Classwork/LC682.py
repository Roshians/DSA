class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        count = 0
        for i in ops:
            if i == "+":
                prev = stack[-1] + stack[-2]
                stack.append(prev)
                count += prev
            elif i == "D":
                prev = stack[-1]*2
                stack.append(prev)
                count += prev
            elif i == "C":
                prev = stack.pop()
                count -= prev
            else:
                stack.append(int(i))
                count += int(i)
        return count