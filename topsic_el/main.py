#品切れ

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(N):
    if A[i] < B[i]:
        ans = i + 1

print(ans)