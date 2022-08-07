N, W =  map(int, input().split())
weights = [0] * (N + 1)
values = [0] * (N + 1)
for i in range(1, N + 1): # インデックスは1から設定
  w, v = map(int, input().split())
  weights[i] = w
  values[i] = v

# 二次元配列を用いた手法
# dp = [] # dp[i][j]はi番目の品物まで使用した重さjを超えない最大の価値の総和
# for _ in range(N + 1): # DPを適用するために0列目と0行目の値は0に設定する
#   dp.append([ 0 for _ in range(W + 1) ])

# for i in range(1, N + 1):
#   for j in range(1, W + 1):
#     if j >= weights[i]:
#       dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + values[i])
#     else:
#       dp[i][j] = dp[i - 1][j]

# print(dp[N][W]) # N番目の品物までを使用した重さWを超えない最大の価値の総和

# 一次元配列を用いた手法
dp = [0] * (W + 1)
for i in range(1, N + 1):
  for j in reversed(range(1, W + 1)):
    if j >= weights[i]:
      dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
print(dp[W])

# 結果：TLE