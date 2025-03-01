from py_source.graph import *
from cmath import sqrt
import math
import geopy.distance

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
        length=geopy.distance.geodesic((demand_point[1], demand_point[2]),(deports[0][1], deports[0][2])).km
        key=deports[0]
        for i in range(len(deports)-1):
            temp_length = geopy.distance.geodesic((demand_point[1],demand_point[2]),(deports[i+1][1],deports[i+1][2])).km
            if temp_length<length:
                length=temp_length
                key=deports[i+1]
        return_dic[key].append(demand_point)
    
    return return_dic


def create_cluster_graph_list(cluster_dic):
    graph_list=[]
    for x in cluster_dic:
        vertice_list=[x]
        for ele in cluster_dic[x]:
            if x!=ele:
                vertice_list.append(ele)
        
        graph_list.append(Graph(len(vertice_list),vertice_list))
    return graph_list


    
    