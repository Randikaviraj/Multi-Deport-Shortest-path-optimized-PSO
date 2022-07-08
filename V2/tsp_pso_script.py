from py_source.pso import PSO
from py_source.graph import Graph
from py_source.utils import location_loader,edge_loader




file="cluster"
data=location_loader(file)
file="cluster-3-1-edges"
edges=edge_loader()
print(data)
g=Graph(len(data),data)
g.path_town_print()
g.showGraph()
pso = PSO(g, iterations=100, size_population=10, beta=1, alfa=0.9)
print("")
print("---------------particles-----------------------------------")
pso.showsParticles() # shows the particles
print("---------------particles-----------------------------------")
pso.run() # runs the PSO algorithm
# shows the global best particle
print('gbest: %s | cost: %f\n' % (pso.getGBest().getPBest(), pso.getGBest().getCostPBest()))
print("================================================================================")