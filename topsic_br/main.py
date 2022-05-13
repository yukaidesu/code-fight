#数列の操作

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

#Bの正しい順を保管
S = B
A = sorted(A)
B = sorted(B)

calc = 0
change = 0

for i in range(N):
    calc += abs(A[i] - B[i])

change = 0
for i in range(N):
    if S[i] == B[i]:
        change += 1

change = change // 2

print(calc + change)