import sys
def input():
  return sys.stdin.readline()[:-1]

N, W = map(int, input().split())
w_list = [0] * (N+1)
v_list = [0] * (N+1)
for i in range(1, N+1):
  l = list(map(int, input().split()))
  w_list[i] = l[0]
  v_list[i] = l[1]

dp = [ [ 0 for _ in range(W+1) ] for _ in range(N+1) ]
for i in range(1, N+1):
  for j in range(1, W+1):
    if j >= w_list[i]:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-w_list[i]] + v_list[i])
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(str(dp[N][W]))

# 結果:TLE