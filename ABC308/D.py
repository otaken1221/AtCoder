import sys
h, w = map(int, input().split())
s = [input() for _ in range(h)]

flags = [[False for i in range(w)] for j in range(h)]

t = "snuke"
temp = s[0][0]
if temp in t:
    q = t.index(temp)
else:
    print("No")
    sys.exit()
def dfs(x, y, q):
    
    # 範囲外や壁の場合は終了
    if y >= w or y < 0 or x >= h or x < 0 or flags[x][y] or s[x][y] != t[q]:
        return

    # ゴールに辿り着ければ終了
    if x == h-1 and y == w-1:
        print('Yes')
        sys.exit()
        

    flags[x][y] = True # 確認したルートは壁にしておく
    l = (q + 1) % len(t)
    # 上下左右への移動パターンで再起していく
    dfs(x+1, y,l)
    dfs(x-1, y,l)
    dfs(x, y+1,l)
    dfs(x, y-1,l)

dfs(0, 0, q) # スタート位置から深さ優先探索
print('No')

