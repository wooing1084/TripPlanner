from test2 import result
from test2 import arr
import pandas as pd
class Attributes:
    # desinations list
    addressList = arr
    # 3D Adjacent matrix
    apiResult = result
    #Result path(after algorithm)
<<<<<<< HEAD
    path = []
    

    df=pd.Series(result)
    print(apiResult)
    print(f"results{apiResult[1]}")
    print(f"addressList{arr}")
    dff= pd.Series(df)
    time =[]
    distance=[]
    n=5
    for y in range(n):
         for x in range(n):
           time.append (dff[y][x][0])
           distance.append (dff[y][x][1])
    
    dict = {'time': time,
        'Distance': distance}
 
    # creating a dataframe from dictionary
    df = pd.DataFrame(dict)
    a=df.iloc[0:5].reset_index(drop=True)
    b=df.iloc[5:10].reset_index(drop=True)
    c=df.iloc[10:15].reset_index(drop=True)
    d=df.iloc[15:20].reset_index(drop=True)
    e=df.iloc[20:25].reset_index(drop=True)
    result = pd.concat([a,b,c,d,e],axis=1 )
    print(result)
=======
    path = []    
    n = 0
    carType = '3'
    fPercent = 0
    pMileage = 0
>>>>>>> 417f59984bb958c03b82611cbcde51556754893c
