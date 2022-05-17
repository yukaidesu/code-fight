#三角形の相似
# 解答まち
import itertools
xy1 = [list(map(int, input().split())) for _ in range(3)]
xy2 = [list(map(int, input().split())) for _ in range(3)]

xy1_comb = itertools.combinations(xy1, 2)
lines_1 = []
for i in xy1_comb:
    #print(i)
    lines_1.append(((i[0][0] - i[1][0]) ** 2 + (i[0][1] - i[1][1]) ** 2) ** 0.5)

xy2_comb = itertools.combinations(xy2, 2)
lines_2 = []
for i in xy2_comb:
    #print(i)
    lines_2.append(((i[0][0] - i[1][0]) ** 2 + (i[0][1] - i[1][1]) ** 2) ** 0.5)

lines_1.sort()
lines_2.sort() # sortすることでどの辺とどの辺を比べればいいかわかる

#print(lines_1)
#print(lines_2)

rates = [] # それぞれの比率
for i in range(3):
    rates.append(lines_1[i] / lines_2[i])
#print(rates)

if rates[0] == rates[1] and rates[1] == rates[2]:
    print("YES")
else:
    print("NO")