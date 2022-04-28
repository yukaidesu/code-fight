#変化するモンスターの名前

S = input()
N = int(input())
name = list(reversed(S))
a = [""] * N


for i in range(N):
    a[i] = "a"

rename = ''.join(list(reversed(name)))
ans = ''.join(a) + rename
print(ans)