n = input()
s = 0
for i in n:
    if i == '4' or i == '7':
        s += 1
if s == 4 or s == 7:
    print("YES")
else: print("NO")