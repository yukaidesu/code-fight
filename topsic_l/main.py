#三角形の相似

xy = [list(map(int, input().split())) for _ in range(3)]
xy2 = [list(map(int, input().split())) for _ in range(3)]

ans = True
for i in range(3):
    for j in range(2):
        if xy[i][j] > xy2[i][j]:
            if xy2[i][j] != 0:
                #print(f"{xy[i][j]}ワル{xy2[i][j]}あまりがゼロ")
                if xy[i][j] % xy2[i][j] != 0:
                    ans = False
        else:
            if xy[i][j] != 0:
                #print(f"{xy2[i][j]}ワル{xy[i][j]}あまりがゼロ")
                if xy2[i][j] % xy[i][j] != 0:
                    ans = False

if ans:
    print("YES")
else:
    print("NO")