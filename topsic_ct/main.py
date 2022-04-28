#右折

N = int(input())
d = [int(input()) for _ in range(N)]
kisuu = []
guusuu = []

#右左に移動
rile = 0
#上下に移動
updown = 0

for i in range(N):
    if i % 2 == 0:
        kisuu.append(d[i])
    else:
        guusuu.append(d[i])

for i in range(len(kisuu)):
    if i % 2 == 0:
        rile += kisuu[i]
    else:
        rile -= kisuu[i]

for i in range(len(guusuu)):
    if i % 2 == 0:
        updown -= guusuu[i]
    else:
        updown += guusuu[i]

print(rile, updown)