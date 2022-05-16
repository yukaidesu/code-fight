# 凸

n = int(input())
a = list(map(int, input().split()))
ans = True

for i in range(n - 2):
    #print(f"{a[i + 2]}と{a[i]}")
    if (a[i + 2] + a[i]) / 2 >= a[i + 1]:
        ans = False
        break

if ans:
    print("YES")
else:
    print("NO")