# COM Server  
import pythoncom
import math
from joblib import load
import numpy as np
import os

import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'dummy_clf.joblib')
clf = load(filename) 

def convert_data(data, period):
    data = np.array(data)
    indexer = np.arange(period)[None, :] + (np.arange(data.shape[0])[:, None] - (period - 1))
    indexer[indexer < 0] = 0
    return data[indexer]

def create_df(data_array, period):
    result = np.array(convert_data(list(data_array[0]), period))
    for data in data_array[1:]:
        data = list(data)
        result = np.append(result, convert_data(data, period), axis = 1)
    return result

def normalize(data):
    max_ = np.amax(data, 1).T.reshape(-1, 1)
    min_ = np.amin(data, 1).T.reshape(-1, 1)
    range_ = max_ - min_
    data = (data - min_)/range_ 
    return data


class ABTestObj:
    _public_methods_ = ["MyABMethod"]   #your public method
    _reg_progid_ = "ABTest.main"   # name of your com server
    # use pythoncom.CreateGuid()  to create your ID
    _reg_clsid_ = "{F5073AA0-DC4C-4909-8EC0-4A3E1F025912}" # create/register COM GUID

    def MyABMethod(self, o, h, l, c):
        arr = create_df([o, h, l, c], 30)
        arr = normalize(arr)
        arr = np.nan_to_num(arr)
        y_pred = clf.predict_proba(arr).T[1]
        
        predict_reshape = y_pred.reshape(-1, 1)

        return predict_reshape.tolist()

if __name__ == "__main__":
    # run "python server.py 
    #    register the COM server
    # run "python server.py --unregister"
    #    to unregister it
    print("Registering COM server...")
    import win32com.server.register
    win32com.server.register.UseCommandLine(ABTestObj)