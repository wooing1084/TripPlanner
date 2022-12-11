# *-- Geocoding 활용 코드 --*
import json
import sys
import urllib
import requests
from urllib.request import Request, urlopen
import pandas as pd
# *-- 3개의 주소 geocoding으로 변환한다.(출발지, 도착지, 경유지) --*


# 주소에 geocoding 적용하는 함수를 작성.
def get_location(loc) :
    client_id = 'vq5s61guie'
    client_secret = 'c97RkT0yyNKSmX4I4YGUjnaSMjCEzzh3uc2gs5ht'
    url = f"https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query=" \
    			+ urllib.parse.quote(loc)
    
    # 주소 변환
    request = urllib.request.Request(url)
    request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
    request.add_header('X-NCP-APIGW-API-KEY', client_secret)
    
    response = urlopen(request)
    res = response.getcode()
    
    if (res == 200) : # 응답이 정상적으로 완료되면 200을 return한다
        response_body = response.read().decode('utf-8')
        response_body = json.loads(response_body)
        # print(response_body)
        # 주소가 존재할 경우 total count == 1이 반환됨.
        if response_body['meta']['totalCount'] == 1 : 
        	# 위도, 경도 좌표를 받아와서 return해 줌.
            lat = response_body['addresses'][0]['y']
            lon = response_body['addresses'][0]['x']
            return (lon, lat)
        else :
            print('location not exist')
        
    else :
        print('ERROR')
        

######################################################################################################################################################

# *-- Directions 5 활용 코드 --*
option = 'traoptimal'

def get_optimal_route(start, goal, carVal, option=option) :
    client_id = 'vq5s61guie'
    client_secret = 'c97RkT0yyNKSmX4I4YGUjnaSMjCEzzh3uc2gs5ht' 

    url = f"https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving?start=" + start[0] + "," + start[1] + "&goal=" + goal[0] + "," +  goal[1] + "&option=" + option + "&cartype=" + carVal
    request = urllib.request.Request(url)
    request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
    request.add_header('X-NCP-APIGW-API-KEY', client_secret)
    
    response = urllib.request.urlopen(request)
    res = response.getcode()
    
    if (res == 200) :
        response_body = response.read().decode('utf-8')
        return json.loads(response_body)
            
    else :
        print('ERROR')


#print("total_distance : ", results['route']['traoptimal'][0]['summary']['distance'], "duration", results['route']['traoptimal'][0]['summary']['duration'])

def get_time(location, carval = '1') :
    
    locations = make_input(location)
    sizeof_input = len(locations)
    print(len(locations))
    list_re = [[0 for j in range(2)] for i in range(len(locations))]
    for count in range(0, sizeof_input):
        start = get_location(locations[count][0])
        goal = get_location(locations[count][1])
        # print(location[count][0], ' ', location[count][1], ' ', start, ' ', goal)
        option = 'traoptimal'
        results = get_optimal_route(start, goal, carval, option)
        total_distance = results['route']['traoptimal'][0]['summary']['distance']
        total_duration = results['route']['traoptimal'][0]['summary']['duration']
        list_re[count][0] = round(total_duration / 1000)
        list_re[count][1] = round(total_distance / 1000)
        # print(list_re[count][0], ' ', list_re[count][1]) 
    
    return list_re


def make_input(location):
    
    matrix = []
    for i in range(len(location)):
        for j in range(len(location)):
            if i == j:
                continue
            matrix.append([location[i], location[j]])
            
    return matrix

def make_matrix(list, dests):
    result = []

    k = 0
    for i in range(dests + 1):
        temp = []
        for j in range(dests + 1):

            if i == 0:
                temp.append([float('inf'), float('inf')])
            else:
                if j == 0:
                    temp.append([float('inf'), float('inf')])

                elif i == j:
                    temp.append([0, 0])
                else:
                    temp.append(list[k])
                    k += 1
        
        result.append(temp)
        
    result[0][0] = [0,0]
    result[0][1] = [0,0]
    #result[0][dests] = [0,0]
    
    result[1][0] = [0,0]
    result[dests][0] = [0,0]
    return result
                
                
            
    