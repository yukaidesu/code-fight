#互いに異なる
n = int(input())
a = list(map(int, input().split()))

flag = False
for i in range(n):
    for j in range(i+1, n):
        if a[i] == a[j]:
            flag = True

if flag:
    print("NO")
else:
    print("YES")