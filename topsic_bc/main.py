#文字の数
import collections

S = input()

c = collections.Counter(S)

print(len(c))