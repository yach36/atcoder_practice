N, K = map(int, input().split())
h = [ int(height) for height in input().split() ]

# dp[i]はi番目の足場に行くまでの最小コスト
dp = [ float('inf') ] * N
dp[0] = 0 # 1番目の足場へのコストは0
dp[1] = abs(h[1] - h[0]) # 0番目から1番目に行くルートは1通り

# 2番目以降の足場はどのルートが最もコストが小さいかを比較する
for i in range(2, N):
  costs = []
  if i < K:
    for j in range(i):
      costs.append(dp[j] + abs(h[i] - h[j]))
  else:
    for j in range(i - K, i):
      costs.append(dp[j] + abs(h[i] - h[j]))
  dp[i] = min(costs)

print(dp[N - 1])

# 結果：TLE