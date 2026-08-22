arr = [30,2,8,18,17,31,54]
odd = 0
even = 0
for i in arr:
    if not(i%2):
        even += 1
    else:
        odd += 1

print(f"Odd = {odd}, Even = {even}")
