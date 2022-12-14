from math import floor
import pandas as pd
class Attributes:
    # desinations list
    addressList = []
    carType = '3'
    fPercent = 0
    pMileage = 0
    #--------- Before API
    # 3D Adjacent matrix
    apiResult = []
    #-----------After API
    #---------- Algorithm
    n = 0
    path = []    
    totalTime = 0
    totalDistance = 0

    
    def secToHour(time):
        h = floor(time / 3600)
        time %= 3600
        m = floor(time / 60)
        
        return str(h) + "시간 " + str(m) + "분 "

    
    def GetResult(self):
        print(self.apiResult)
        print(f"addressList{self.addressList}")
        
        nodeInfos = []
        
        
        src = self.path[0]
        dest = self.path[0]
        self.totalDistance = 0
        self.totalTime = 0


        for i in range(self.n):
            dest = self.path[i]

            if i == self.n - 1:
                icon = "icon/end_P.png"
            elif i == 0:
                icon = "icon/start_P.png"
            else:
                icon = "icon/Kyoung_" + str(i) +".png"
            
            self.totalDistance += self.apiResult[src][dest][1]
            self.totalTime += self.apiResult[src][dest][0]
            node = {"index_Num": str(i + 1) ,"point_Name": str(self.addressList[i]) ,"interval_Distance": str(self.apiResult[src][dest][1]), "cumulative_Distance": str(self.totalDistance) ,"interval_Time": self.secToHour(self.apiResult[src][dest][0]) ,"cumulative_Time": self.secToHour(self.totalTime) ,"Num_Photo":icon}
            
            
            
            src = dest
            
            nodeInfos.append(node)
        print(nodeInfos)
        
        return nodeInfos
            
                
        # creating a dataframe from dictionary
        # df = pd.DataFrame(dict)
        # a=df.iloc[0:5].reset_index(drop=True)
        # b=df.iloc[5:10].reset_index(drop=True)
        # c=df.iloc[10:15].reset_index(drop=True)
        # d=df.iloc[15:20].reset_index(drop=True)
        # e=df.iloc[20:25].reset_index(drop=True)
        # result = pd.concat([a,b,c,d,e],axis=1 )
        # print(result)

