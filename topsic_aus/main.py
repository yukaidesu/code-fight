#ジャングルジム

N = int(input())
A = list(map(int, input().split()))
left = [0 for _ in range(N)]
left_tired = 0
right = [0 for _ in range(N)]
right_tired = 0

#左から登る
for i in range(N - 1):
    left[i] = (A[i+1]-A[i])
    if left[i] >= 0:
        left_tired += left[i]

#右から登る
for i in reversed(range(1, N)):
    right[i] = (A[i-1]-A[i])
    if right[i] >= 0:
        right_tired += right[i]

if left_tired < right_tired:
    print(left_tired)
else:
    print(right_tired)