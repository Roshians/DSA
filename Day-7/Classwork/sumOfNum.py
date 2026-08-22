def sum(n):
    if n == 1:
        return 1
    elif n ==0:
        return 0
    return n + sum(n-1)

inp = int(input())
print(sum(inp))