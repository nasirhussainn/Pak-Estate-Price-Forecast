import json
import pickle
import numpy as np

__location =  None
__data_columns = None
__model = None

    
def get_location_names():
    return __location

def load_saved_artifact():
    print("Loading saved artifacts...start")
    global __data_columns
    global __location
    global __model
    
    with open("./artifact/columns.json",'r') as f:
        __data_columns=json.load(f)['data_columns']
        __location=__data_columns[3:]
        
    with open("./artifact/Lahore_House_Model.pickle",'rb') as f:
        __model=pickle.load(f)
        print(type(__model))
        print("Loading saved artifact...done")


def predicted_price(location,bedroom,baths,area):
    try:
        loc_index=__data_columns.index(location.lower)
    except:
        loc_index = -1
    
    x=np.zeros(len(__data_columns))
    x[0]=baths
    x[1]=bedroom
    x[2]=area
    if(loc_index>=0):
        x[loc_index]=1 
    return round(__model.predict([x])[0],2)  


if __name__=='__main__':
    load_saved_artifact()
    #print(get_location_names())    
    #print(predicted_price('al rehman garden', 3, 3, 2000))
    