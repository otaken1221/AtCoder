n = int(input())
temp = input()

flag=False
start = 0
end_flag = False
while(1):
  flag=False
  if temp == "":
        break
  for i,t in enumerate(temp):
      if t == "(":
          if not flag:
            flag=True
          start = i
          if not(")" in temp[start+1:]):
            end_flag=True
            break 
          
      elif t == ")":
        if flag:
            temp = temp[:start] + temp[i+1:]
            break
      if not(")" in temp):
            end_flag=True
            break  
      if i==len(temp)-1:
        end_flag=True
        
  if end_flag:
    break

print(temp)