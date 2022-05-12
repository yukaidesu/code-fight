#決議

N, G, A = map(int, input().split())
#　(N × G)人で決議　63
#　賛成は(A)人、反対は(N × G - A)人　41、22
# (N)人のグループを(G)個ー＞過半数賛成の場合賛成グループ　7人　×9　過半数4
# 過半数は(N // 2) + 1

if A // (N // 2 + 1) > G:
    large = G
else:
    large = A // (N // 2 + 1)

small = G - ((N * G - A) // (N // 2 + 1))

print(large, small)