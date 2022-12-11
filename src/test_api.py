# *-- Geocoding 활용 코드 --*
import webview
import json
import urllib
import requests
import folium
from urllib.request import Request, urlopen
import pandas as pd
import folium


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

def get_optimal_route(start, goal, carVal = '3', option='traoptimal') :
    client_id = 'vq5s61guie'
    client_secret = 'c97RkT0yyNKSmX4I4YGUjnaSMjCEzzh3uc2gs5ht' 

    url = f"https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving?start=" + str(start[0]) + "," + str(start[1]) + "&goal=" + str(goal[0]) + "," +  str(goal[1]) + "&option=" + str(option) + "&cartype=" + str(carVal)
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

def get_dis_time(location, carval = '3') : 
    sizeof_input = len(location)
    print(len(location))
    list_loc = [[0 for j in range(0, 5)] for i in range(len(location))]
    temp = [[0 for j in range(0, 2)] for i in range(0, len(location))]
    point = [[0 for j in range(0, 2)] for i in range(0, len(location))]
    bigpoint = [0 for i in range(0,2)]
    smallpoint = [0 for i in range(0,2)]
    for i in range(0, sizeof_input):
        temp[i] = get_location(location[i])
        point[i][0] = float(temp[i][0])
        point[i][1] = float(temp[i][1])
        if(i==0):
            bigpoint[1] = point[i][1]
            bigpoint[0] = point[i][0]
            smallpoint[1] = point[i][1]
            smallpoint[0] = point[i][0]
        if(point[i][0] > bigpoint[0]):
            bigpoint[0] = point[i][0]
        if(point[i][1] > bigpoint[1]):
            bigpoint[1] = point[i][1]
        if(point[i][0] < smallpoint[0]):
            smallpoint[0] = point[i][0]
        if(point[i][1] < smallpoint[1]):
            smallpoint[1] = point[i][1]
        print(i)
    center = [(smallpoint[1] + bigpoint[1]) / 2, (bigpoint[0] + smallpoint[0]) /2]
    m = folium.Map(location=center, zoom_start=10)
    path = []
    for count in range(0, sizeof_input) :
        if(count==0): # 처음일 경우
            list_loc[count][0] = location[0]
            for i in range (1, 5):
                list_loc[count][i] = 0
        else: # 2 ~ n 번째
            results = get_optimal_route(point[count-1], point[count], carval)
            path = results['route']['traoptimal'][0]['path'] # 에러발생(in. get_dis_time)
            location_data = [[0 for col in range(2)] for row in range(len(path)-1)]
            for i in range (0,len(path) - 1):
                location_data[i][0] = path[i][1]
                location_data[i][1] = path[i][0]
            folium.PolyLine(locations=location_data, tooltip='Polyline').add_to(m)
            list_loc[count][0] = location[count]
            list_loc[count][1] = int(results['route']['traoptimal'][0]['summary']['distance']) / 1000   # km 단위 (기본단위는 m, 1000으로 나누었으므로 km 단위. 나머지 값은 소수점으로 나옴.)
            list_loc[count][2] = list_loc[count-1][2] + list_loc[count][1]
            list_loc[count][3] = int(results['route']['traoptimal'][0]['summary']['duration']) // 1000  # 초 단위 (기본단위는 ms, 1000으로 나누었으므로 초 단위. 1초보다 작은 값은 버림.)
            list_loc[count][4] = list_loc[count-1][4] + list_loc[count][3]
    m.save('save.html')
    return list_loc

def show_html():
    window = webview.create_window('result', "save.html")
    webview.start()


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
                
def get_dis_time(location, carval = '1') :
    sizeof_input = len(location)
    print(len(location))
    list_loc = [[0 for j in range(0, 5)] for i in range(len(location))]
    temp = [[0 for j in range(0, 2)] for i in range(0, len(location))]
    point = [[0 for j in range(0, 2)] for i in range(0, len(location))]
    bigpoint = [0 for i in range(0,2)]
    smallpoint = [0 for i in range(0,2)]
    for i in range(0, sizeof_input):
        temp[i] = get_location(location[i])
        point[i][0] = float(temp[i][0])
        point[i][1] = float(temp[i][1])
        if(i==0):
            bigpoint[1] = point[i][1]
            bigpoint[0] = point[i][0]
            smallpoint[1] = point[i][1]
            smallpoint[0] = point[i][0]
        if(point[i][0] > bigpoint[0]):
            bigpoint[0] = point[i][0]
        if(point[i][1] > bigpoint[1]):
            bigpoint[1] = point[i][1]
        if(point[i][0] < smallpoint[0]):
            smallpoint[0] = point[i][0]
        if(point[i][1] < smallpoint[1]):
            smallpoint[1] = point[i][1]
        print(i)
    center = [(smallpoint[1] + bigpoint[1]) / 2, (bigpoint[0] + smallpoint[0]) /2]
    m = folium.Map(location=center, zoom_start=10)
    path = []
    for count in range(0, sizeof_input) :
        if(count==0): # 처음일 경우
            list_loc[count][0] = location[0]
            for i in range (1, 5):
                list_loc[count][i] = 0
        else: # 2 ~ n 번째
            results = get_optimal_route(point[count-1], point[count])
            path = results['route']['traoptimal'][0]['path'] # 에러발생(in. get_dis_time)
            location_data = [[0 for col in range(2)] for row in range(len(path)-1)]
            for i in range (0,len(path) - 1):
                location_data[i][0] = path[i][1]
                location_data[i][1] = path[i][0]
            folium.PolyLine(locations=location_data, tooltip='Polyline').add_to(m)
            list_loc[count][0] = location[count]
            list_loc[count][1] = int(results['route']['traoptimal'][0]['summary']['distance']) / 1000   # km 단위 (기본단위는 m, 1000으로 나누었으므로 km 단위. 나머지 값은 소수점으로 나옴.)
            list_loc[count][2] = list_loc[count-1][2] + list_loc[count][1]
            list_loc[count][3] = int(results['route']['traoptimal'][0]['summary']['duration']) // 1000  # 초 단위 (기본단위는 ms, 1000으로 나누었으므로 초 단위. 1초보다 작은 값은 버림.)
            list_loc[count][4] = list_loc[count-1][4] + list_loc[count][3]
    m.save('save.html')
    return list_loc

            
    