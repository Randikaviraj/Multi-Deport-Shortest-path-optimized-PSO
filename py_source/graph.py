import random, sys, math

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
            print('%d linked in %d with cost %d' % (edge[0], edge[1], self.edges[edge]))
    
    def __init__(self, amount_vertices,vertices_list):
        self.edges = {} 
        self.vertices = set() 
        self.amount_vertices = amount_vertices 
        self.vertices_list= vertices_list


        for i in range(len(vertices_list)):
            self.vertices.add(i)
            for j in range(len(vertices_list)):
                if i!=j:
                    self.edges[(i, j)]=math.sqrt(math.pow(vertices_list[i][1]*10000-vertices_list[j][1]*10000,2)+math.pow(vertices_list[i][2]*10000-vertices_list[j][2]*10000,2))






	# gets random unique paths - returns a list of lists of paths
    def getRandomPaths(self, max_size):

        random_paths, list_vertices = [], list(self.vertices)

        initial_vertice = random.choice(list_vertices)
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