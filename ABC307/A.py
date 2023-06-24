n = int(input())
a = map(int, input().split())
a_work=[0 for i in range(n)]
for i, w in enumerate(a):
    a_work[int(i/7)] += w

for i in range(len(a_work)):
    a_work[i] = str(a_work[i])
print(" ".join(a_work))