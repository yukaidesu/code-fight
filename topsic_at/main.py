#決議

N, G, A = map(int, input().split())
#　(N × G)人で決議　                                　113229×3=339687　　　　　　　　　　　 7×9=63
#　賛成は(A)人、反対は(N × G - A)人　                  賛成37077、反対302610　　　　　　　　　賛41、反対22
# (N)人のグループを(G)個ー＞過半数賛成の場合賛成グループ　　賛成過半数56615 反対 56614　　　      賛4、反3
# 過半数は(N // 2) + 1


if A // (N // 2 + 1) > G:
    large = G
else:
    large = A // (N // 2 + 1)

#print(f"合計反対人数{N * G - A}、反対過半数{N - (N // 2 + 1)}")
#print(f"{(N * G - A) // (N - (N // 2 + 1))}でGが{G}")
if N <= 1:
    small = G - ((N * G - A) // (N // 2 + 1))
else:
    if (N * G - A) // (N - (N // 2 + 1)) > G:
        small = 0
    else:
        small = G - ((N * G - A) // (N // 2 + 1))

print(large, small)