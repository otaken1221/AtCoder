n = int(input())

s = []
for i in range(n):
    s.append(input())

flag = False

for _ in range(n):
  for i in range(_,len(s)):
     try:
      temp = s
      s = list(set(s))
      s[i] = s[i][::-1]
  
      s = list(set(s))
      s[i] = s[i][::-1]

      if i == len(s) -1:
          flag = True
      if set(s) ^ set(temp) != set([]):
          break
     except IndexError:
        break
     
  if flag:
     break

print(len(s))

# TLE