import random
import numpy as np
import geopy.distance

def location_loader(file_name):
    return_array=[]
    f = open(file_name)
    while True:
        line = f.readline()
        if not line:
            break
        split_list=line.split(",")
        tuf=(split_list[0],float(split_list[1]),float(split_list[2]),float(split_list[3]),float(split_list[4]))
        return_array.append(tuf)
    return return_array

def edge_loader(file_name):
    return_dic={}
    f = open(file_name)
    while True:
        line = f.readline()
        if not line:
            break
        split_list=line.split(",")
        return_dic[(int(split_list[0]), int(split_list[1]))]=float(split_list[2])
        return_dic[(int(split_list[1]),int(split_list[0]))]=float(split_list[2])

    return return_dic





class KMeans:
  def __init__(self, n_clusters=8, max_iter=300,initial_centroids=[]):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.centroids=initial_centroids
        self.sorted_points={}

  def geo_distance(self,point, centroids):
    """
    geo_distance distance between point & data.
    """
    dist_from_sentroid=0
    return_centroid=()
    for centroid in centroids:
        val=geopy.distance.geodesic((point[1],point[2]),(centroid[0],centroid[1])).km
        if dist_from_sentroid  < val:
            dist_from_sentroid=val
            return_centroid=centroid
    return return_centroid


  def fit(self, X_train):        
        # Randomly select centroid start points, if not set
        
        if not len(self.centroids):
            for _ in range(self.n_clusters):
                ele=random.choice (X_train)
                while (ele[1],ele[2])  in self.centroids:
                    ele=random.choice (X_train)
                self.centroids.append((ele[1],ele[2]) )
        # Iterate, adjusting centroids until converged or until passed max_iter
        iteration = 0
        prev_centroids = None
        while np.not_equal(self.centroids, prev_centroids).any() and iteration < self.max_iter:
            self.sorted_points={}
            for x in X_train:
                centroid_idx = self.geo_distance(x, self.centroids)
                self.sorted_points.setdefault(centroid_idx, []).append(x)

            # Push current centroids to previou
            # s, reassign centroids as mean of the points belonging to them
            prev_centroids = self.centroids
            self.gravity_model(self.sorted_points)
            iteration += 1

  def gravity_model(self,sorted_points):
    for key in sorted_points:
        demand_values=0
        demand_val_mul_x=0
        demand_val_mul_y=0
        for demand_point in sorted_points[key]:
            demand_values=demand_values+demand_point[3]
            demand_val_mul_x=demand_val_mul_x+demand_point[1]*demand_point[3]
            demand_val_mul_y=demand_val_mul_y+demand_point[2]*demand_point[3]
        self.centroids[self.centroids.index(key)]=(demand_val_mul_x/demand_values,demand_val_mul_y/demand_values)

  def get_cluster(self):
    return self.sorted_points
        