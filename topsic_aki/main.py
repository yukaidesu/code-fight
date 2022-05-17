# ほぼ昇順
N = int(input())
S = input()

temp = ["" for _ in range(N)]
ans = 0

for i in range(N):
    temp[i] = S.replace(S[i], '')
    if temp[i] == ''.join(sorted(temp[i])):
        ans = i + 1
        break
    else:
        ans = -1

print(ans)