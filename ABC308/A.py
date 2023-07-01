s = map(int, input().split())

flag = True

for i,t in enumerate(s):

    if i != 0:
        if temp > t:
            flag = False
        temp = t
    else:
        temp = t
        
    
    if t < 100 or t >675:
        flag = False
        
    if t % 25 != 0:
        flag = False
  
if flag:
    print("Yes")

else:
    print("No")