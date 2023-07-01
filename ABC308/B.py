n, m = map(int, input().split())

c = input().split()
d = input().split()
p = list(map(int, input().split()))
money = 0
for i,t in enumerate(c):
    if t in d:
        idx = d.index(t) + 1
    else:
        idx = 0
    money += p[idx]

print(money)
