# api 불러오는 형식
from TSP_2 import Algorithm
from test_api import get_time, make_matrix

# 저장된 2차원 배열 [[출발지1, 목적지1],[출발지2, 목적지2],[출발지3, 목적지3], ... [출발지n, 목적지n]]
arr = [0 for j in range(4)]
value = [[0 for j in range(2)] for i in range(2)] # 값을 받을 문자열도 동일하게 생성하기
# arr[0][0] = '서울 노원구 동일로 1308-1'
# arr[0][1] = '경기 성남시 수정구 성남대로 1332'
# arr[1][0] = '서울 강남구 선릉로158길 10'
# arr[1][1] = '서울 금천구 시흥대로141길 81'
arr[0] = '서울 노원구 동일로 1308-1'
arr[1] = '경기 성남시 수정구 성남대로 1332'
arr[2] = '서울 강남구 선릉로158길 10'
arr[3] = '서울 금천구 시흥대로141길 81'
value = get_time(arr, '3') # carval은 톨게이트 요금 계산용 차종 정보를 나타내는 코드.

result = make_matrix(value, 4)

#테스트할때 API호출 횟수가 많으니 한번 쓴거 재사용하자
# result = [[[0, 0], [0, 0], [float('inf'), float('inf')], [float('inf'), float('inf')], [float('inf'), float('inf')]], 
#           [[0, 0], [0, 0], [3593.688, 33021], [2942.683, 19101], [4649.855, 35813]],
#           [[float('inf'), float('inf')], [3302.727, 29687], [0, 0], [2575.093, 16188], [3174.58, 31295]], 
#           [[float('inf'), float('inf')], [1613.749, 18121], [1653.306, 14930], [0, 0], [2861.655, 19150]], 
#           [[0, 0], [3789.645, 32665], [2731.982, 33745], [3537.67, 18917], [0, 0]]]

print(result)
print("\n")

alg = Algorithm()
alg.n = 5
alg.graph = result
alg.dp = [[alg.INF] * (1 << alg.n) for _ in range(alg.n)]

print(alg.dfs(0,1))
print(alg.printPath(0,1))