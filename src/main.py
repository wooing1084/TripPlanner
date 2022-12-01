import sys

input = sys.stdin.readline
n = int(input())
cities = [list(map(int, input().split())) for _ in range(n)]

VISITED_ALL = (1 << n) - 1

cache = [[None] * (1 << n) for _ in range(n)]
INF = float('inf')

def find_path(last, visited):
    if visited == VISITED_ALL:
        return cities[last][0] or INF  

    if cache[last][visited] is not None:
        return cache[last][visited]

    tmp = INF
    for city in range(n):
        if visited & (1 << city) == 0 and cities[last][city] != 0:
            tmp = min(tmp, find_path(city, visited | (1 << city)) + cities[last][city])
    cache[last][visited] = tmp
    return tmp


print(find_path(0, 1 << 0))

# input
# 4
# 0 20 28 30
# 25 0 27 28
# 30 35 0 29
# 280 29 27 0

# output
# 105