# 凸

n = int(input())
a = list(map(int, input().split()))
ans =[False for _ in range(n)]

for i in range(1, n - 1):
    if (a[i] > a[i - 1]) and (a[i] > a[i + 1]):
        ans[i] = True
    else:
        if a[i - 1] > a[i + 1]:
            if (a[i - 1] - a[i + 1]) / 2 < (a[i] - a[i + 1]):
                ans[i] = True

trueans = "YES"
for i in range(1, n - 1):
    if ans[i] == True:
        trueans = "YES"
    else:
        trueans = "NO"

print(trueans)
