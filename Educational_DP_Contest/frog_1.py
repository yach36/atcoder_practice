N = int(input())
h = [ int(height) for height in input().split() ]
dp = [float('inf')] * N
dp[0] = 0 # 1番目の足場に行くのにかかるコストは0
dp[1] = abs(h[1] - h[0]) # 2番目の足場に行く方法は1番目からの方法しかない
for i in range(2, N):
  dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]), dp[i - 2] + abs(h[i] - h[i - 2]))
print(dp[N - 1])