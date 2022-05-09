# タイピングの秒数算出

S = input()
K = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']

tap = len(S)
move = 0
now_position = 0

for i in range(len(S)):
    for j in range(len(K)):
        if K[j] == S[i]:
            #print(f"Sは{S[i]}でKは{K[j]}")
            #print(f"今いるのは{now_position}で、{j}までいくと")
            if now_position > j:
                move += now_position - j
            elif now_position < j:
                move += j - now_position
            #print(f"{move}動くで")
            now_position = j

ans = tap + move
print(ans)