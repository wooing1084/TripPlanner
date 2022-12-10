
# mCurrent: 주행가능 거리(Available Distance)
# #fPercent: 잔여량 (Remaining oil)
# w : 순서에 따른 노드간 거리 (distance array by the order)
def GetRefueling(mCurrent, fPercent, w):
    total = 100 / fPercent * mCurrent
    
    n = len(w)
    result = []
    
    
    for i in range(n):
        if(mCurrent <= w[i]):
            result.append(i)
            mCurrent = total
            
        mCurrent -= w[i]
        
    return result
          