#小銭の組合わせ

n = int(input())
ans = 0

if n % 100 == 0:
    ans = (n // 500) + ((n % 500) // 100)
else:
    ans = -1


print(ans)