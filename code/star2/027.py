N = int(input())

# 登録されたユーザリスト
users = set()
for i in range(1, N+1):
    si = input()
    # 申請ユーザsiがすでにusersに登録されているか
    if si not in users:
        users.add(si)
        print(i)