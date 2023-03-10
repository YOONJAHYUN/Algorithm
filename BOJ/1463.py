# 1로 만들기

# N = 1일때 0 (계산을 안해도됨)
# N = 2일때 1 (2로 나눠주면 1로됨)
# N = 3일때 1 (3으로 나눠주면 1로됨)
# N = 4일때 2
# N = 5일때 3
# N = 6일때 2


import sys

input = sys.stdin.readline

N = int(input())

# 최소값의 경로를 저장하기 위해 dp라는 배열을 선언한다.
# 한번 계산한 문제는 다시 계산하지 않도록 한다.

# 0은 단순 인덱스를 맞추기 위해, 나머지는 N이 1일때 출력값, N이 2일때의 출력값, N이 3일때의 출력값
dp = [0, 0, 1, 1]

# 그래서 4부터 시작해본다.

# 최소값을 비교하기 위한 조건은 3가지
# 2로나누기
# 3으로 나누기
# 1빼기
for i in range(4, N+1):
    # 이전값에 1을 더한거
    dp.append(dp[i-1]+1)
    # 근데 만약 2로 나눠 떨어지면
    # 이전값에 1을 더한것과, 인덱스 2나눈거에 1더한 값 중 더 작은 값을 반환한다.
    if i%2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])
    # 만약에 또 3으로 나눠 떨어지면
    # 이전 값에 1더한 것과, 인덱스 3으로 나눈거에 1더한 값 중 더 작은 값을 반환한다.
    if i%3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])

print(dp[N])
# 풀긴 풀었는데, 사람들은 이 공식을 어케 찾았을까..
