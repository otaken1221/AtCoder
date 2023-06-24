n = int(input())
s = ["" for i in range(n)]
for i in range(len(s)):
    s[i] = input()

flag=False
for i in range(len(s)):
  for j in range(len(s)):
      if i!=j:
          t = s[i] + s[j]
          t_r = t[::-1]
          if t==t_r:
              flag=True
    
if flag:
  print("Yes")
else:
  print("No")