from py_source.knapsack import findRoutes
from py_source.utils import location_loader

file="demand_points-1"
data=location_loader(file)
findRoutes(data,77,(7.0727, 80.0158))