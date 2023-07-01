q = int(input())

brack = []
temp = []
for _ in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        brack.append(query[1])
    
    elif query[0] == 2:
        for i in range(len(brack)):
            if brack[i] == query[1]:
                brack.pop(i)
                break
    
    elif query[0] == 3:
        t = []
        for i in range(len(brack)):
            for j in range(i+1, len(brack)):
                t.append(brack[i] ^ brack[j])
        t.sort()
        temp.append(t[0])
                
for i in temp:
    print(temp)