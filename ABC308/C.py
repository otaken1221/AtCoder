n = int(input())
person = {}
for i in range(n):
    a, b = list(map(int, input().split()))

    p = a / (a + b)

    person[i+1] = p

person_sort = sorted(person.items(), key=lambda x:x[1], reverse=True)

print(" ".join(str(t[0]) for t in person_sort))
