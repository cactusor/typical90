from collections import deque

Q = int(input())
que = deque()
for i in range(Q):
    ti, xi = map(int, input().split())

    # クエリの処理
    if ti == 1:
        que.appendleft(xi)
    elif ti == 2:
        que.append(xi)
    elif ti == 3:
        print(que[xi-1]) # 山札は0番目から始まっているためxi-1