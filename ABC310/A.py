n,p,w = map(int, input().split())
d = list(map(int, input().split()))

discount = w + min(d)

if p < discount:
    print(p)
else:
    print(discount)

# AC