import math
import sys


class Algorithm:
    INF = float('inf')
    graph = [] 
    n = 0
    dp = []
        
    

    # graph[i][j] = graph[j][i] = 점 i와 점 j 사이의 거리
    
    # dp[i][j] : i = 내 위치, j : 아직 방문하지 않은, 방문해야 할 노드 정보
    # 들어가는 값은 남은 점들을 최적 경로로 돌았을 때의 총 거리

    path = []

    def getDist(Ax, Ay, Bx, By):  # 유클리드 거리 반환
        return round(math.sqrt((Ax - Bx) ** 2 + (Ay - By) ** 2), 3)


    def dfs(self, start, visited):
        # start : 현재 내 위치
        # visited : 방문 여부 정보를 담고 있음. 해당 비트가 0이면 방문하지 않은 것, 1이면 방문한 것
        if visited == (1 << self.n) - 1:  # 모든 정점 방문
            self.dp[start][visited] = self.graph[start][0][0]
            return self.graph[start][0][0]

        if self.dp[start][visited] != self.INF:
            return self.dp[start][visited]

        for i in range(1, self.n):
            if visited & (1 << i):  # 0번 점은 시작점이니까 패스하고 1부터 본다. 방문한 점이라면 pass
                continue
            # 그 다음 점까지의 거리 + 그 다음 점에 방문하고 나서 남은 점들을 최적 경로로 돌았을 때의 거리
            # 의 합이 가장 작은 점이 현재 visited 상태 최적 경로 상의 다음 점이 될 것이다.
            self.dp[start][visited] = min(self.dp[start][visited], self.dfs(
                i, visited | (1 << i)) + self.graph[start][i][0])

        return self.dp[start][visited]

    def printPath(self, k, visited):
        # visited 상태에서, 남은 점들을 최적으로 돌 때, 다음으로 방문하는 점을 찾는다.

        if k != 0: 
            self.path.append(k)

        if visited == (1 << self.n) - 1:
            return self.path


        nextvalue = [self.INF, 0]
        for i in range(self.n):
            if visited & (1 << i):
                continue
            # dp[i][visited] 현재 visited에서의 최적이 들어있고, 우리가 찾는건 다음의 최적 점이다.
            # 현재의 visited에 하나씩 비트 붙여가면서 값을 구했을 때, 그 값들 중 최솟값이 다음 최적 점이다.
            if (self.graph[k][i][0] + self.dp[i][visited | (1 << i)]) < nextvalue[0]:
                nextvalue[0] = self.graph[k][i][0] + self.dp[i][visited | (1 << i)]
                nextvalue[1] = i

        # for loop 종료 시, nextvalue[0]에는 남은 점들을 최적으로 돌았을 때의 최소 거리가
        # nextvalue[1]에는 다음 점이 들어 있다

        # 반복.
        return self.printPath(nextvalue[1], visited | (1 << nextvalue[1]))

