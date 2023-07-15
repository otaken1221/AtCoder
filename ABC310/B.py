import sys

n, m = map(int, input().split())
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if i != j:
          if matrix[i][0] >= matrix[j][0]:
              if (set(matrix[i][2::]) & set(matrix[j][2::])) == set(matrix[i][2::]):
                  if (matrix[i][0] > matrix[j][0]) or (set(matrix[i][2::]) & set(matrix[j][2::])) != set(matrix[j][2::]):
                      print("Yes")
                      sys.exit()

print("No")

# AC