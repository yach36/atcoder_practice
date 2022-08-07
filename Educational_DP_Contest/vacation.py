N = int(input())
A = [] # 活動の全種類
for _ in range(N):
  A.append([ int(a) for a in input().split() ])

dp = [] # dp[i][lst] は, i+1日目時点でlst番目の活動を行なったときの幸福度の最大値
for _ in range(N):
  dp.append([ 0 for _ in range(3) ])
# 1日目の幸福度の初期化
for lst in range(3):
  dp[0][lst] = A[0][lst]
# 幸福度の最大値を順に計算
for i in range(1, N):
  for lst in range(3):
    for nxt in range(3):
      if lst != nxt: # 昨日と今日の活動が同じでなければ
        dp[i][nxt] = max(dp[i][nxt], dp[i - 1][lst] + A[i][nxt])
print(max(dp[N - 1]))

# 結果：AC