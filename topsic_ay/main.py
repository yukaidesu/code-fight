#アルファベットの横並べ

N = int(input())
c = [input() for _ in range(N)]

ans = ""
for i in range(N):
    ans += c[i]

print(ans)