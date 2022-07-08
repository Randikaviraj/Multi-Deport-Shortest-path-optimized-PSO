import random, sys, math
import geopy.distance

class Graph:

    def getCostPath(self, path):
        total_cost = 0
        for i in range(self.amount_vertices - 1):
            total_cost += self.edges[(path[i], path[i+1])]
        # add cost of the last edge
        total_cost += self.edges[(path[self.amount_vertices - 1], path[0])]
        return total_cost

    def showGraph(self):
        print('Showing the graph:\n')
        for edge in self.edges:
            print('%d linked in %d with cost %f' % (edge[0], edge[1], self.edges[edge]))
    
    def __init__(self, amount_vertices,vertices_list,edges):
        self.edges = {} 
        self.vertices = set() 
        self.amount_vertices = amount_vertices 
        self.vertices_list= vertices_list
        self.path_list=[]
        self.edges=edges

    def path_town_print(self):
        print("::::Towns::::")
        for x in range(len(self.vertices_list)):
            print(str(x)+" :"+str(self.vertices_list[x][0]))

    def getRandomPaths(self, max_size):

        random_paths, list_vertices = [], list(self.vertices)

        initial_vertice = 0
        if initial_vertice not in list_vertices:
            print('Error: initial vertice %d not exists!' % initial_vertice)
            sys.exit(1)

        list_vertices.remove(initial_vertice)
        list_vertices.insert(0, initial_vertice)

        for i in range(max_size):
            list_temp = list_vertices[1:]
            random.shuffle(list_temp)
            list_temp.insert(0, initial_vertice)

            if list_temp not in random_paths:
                random_paths.append(list_temp)

        return random_paths
        