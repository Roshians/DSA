# Print 1 to n using recursion
def printNum(n):
    if n == 0:
        return
    printNum(n-1)
    print(n)
inp = int(input())
printNum(inp)