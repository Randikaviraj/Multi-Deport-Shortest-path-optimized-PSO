from ast import For
from cmath import sqrt
import math

def location_loader(file_name):
    return_array=[]
    f = open(file_name)
    while True:
        line = f.readline()
        if not line:
            break
        split_list=line.split(",")
        tuf=(split_list[0],float(split_list[1]),float(split_list[2]))
        return_array.append(tuf)
    return return_array

def clustering(demand_points,deports):
    return_dic=dict()
    for point in deports:
        return_dic[point]=[]


    for demand_point in demand_points:
        length=math.sqrt(math.pow(demand_point[1]-deports[0][1],2)+math.pow(demand_point[2]-deports[0][2],2))
        key=deports[0]
        for i in range(len(deports)-1):
            temp_length=math.sqrt(math.pow((demand_point[1]-deports[i+1][1]),2)+math.pow((demand_point[2]-deports[i+1][2]),2))
            if temp_length<length:
                length=temp_length
                key=deports[i+1]
        return_dic[key].append(demand_point)
    
    return return_dic




    
    