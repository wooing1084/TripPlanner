from test2 import result
from test2 import arr
import pandas as pd
class Attributes:
    # desinations list
    addressList = arr
    # 3D Adjacent matrix
    apiResult = result
    #Result path(after algorithm)
    path = []
    

    df=pd.Series(result)
    print(apiResult)
    print(f"results{apiResult[1]}")
    print(f"addressList{arr}")
    df.to_pickle("./dummy.pkl")  