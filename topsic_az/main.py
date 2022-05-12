#マス目の中に文字を追加

H, W, Q = map(int, input().split())
rcs = [input().split() for _ in range(Q)]

S = [ ["."] * W for _ in range(H)]

for i in range(Q):
    S[int(rcs[i][0])-1][int(rcs[i][1])-1] = rcs[i][2]

for j in range(H):
    print("".join(S[j]))

#これは間違え。答え出るけどエラーなる。配列じゃなくて中身だけ出したいから。
# ans = [ "" * W for _ in range(H)]
# if H == 1 and W == 1:
#     print(S[0][0])
# else:
#     for i in range(Q+1):
#         ans[i] = "".join(S[i])
#         print(ans[i])

