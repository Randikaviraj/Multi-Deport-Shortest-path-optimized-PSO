from math import factorial
from py_source.loader import create_cluster_graph_list, location_loader,clustering
from py_source.pso import *


        

if __name__ == "__main__":
    # print(location_loader("demand_points.txt"))
    # print(clustering(location_loader("demand_points.txt"),location_loader("deports.txt")))
    graph_list=create_cluster_graph_list(clustering(location_loader("demand_points.txt"),location_loader("deports.txt")))
    for x in range(len(graph_list)):
        if graph_list[x].amount_vertices==1:
            continue
        graph_list[x].path_town_print()
        # graph_list[x].showGraph()
        # print(graph_list[x].getRandomPaths(10))
        pso = PSO(graph_list[x], iterations=100, size_population=10, beta=1, alfa=0.9)
        # pso.showsParticles() # shows the particles
        pso.run() # runs the PSO algorithm

        # shows the global best particle
        print('gbest: %s | cost: %f\n' % (pso.getGBest().getPBest(), pso.getGBest().getCostPBest()))
    

