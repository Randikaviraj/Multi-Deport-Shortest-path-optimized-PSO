from py_source.utils import location_loader,KMeans
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    file="demand_points"
    data=location_loader(file)
    x=[]
    y=[]
    for d in data:
        x.append(d[1])
        y.append(d[2])

    fig, ax = plt.subplots()
    ax.scatter(x, y)
    #(7.0727, 80.0158),(6.8301, 79.8801),(6.9340, 79.9287) initial
    # (6.926745, 79.8605224),(6.8451342,79.9887083),(6.9559081,79.9169459),(6.83667,79.8439262) cluster 1
    # ( 6.989402,79.885278),(7.12963407, 79.829926) cluster 2
    k=KMeans(initial_centroids=[(7.0727, 80.0158),(6.8301, 79.8801),(6.9340, 79.9287) ])
    k.fit(data)
    data=k.get_cluster()
    cluster_no=1
    for key in data:
        ax.scatter(key[0], key[1],color = 'hotpink')
        print(key)
        with  open(file+"-"+str(cluster_no), "w") as f:
            for tuf in data[key]:
                f.write(str(tuf[0]))
                f.write(",")
                f.write(str(tuf[1]))
                f.write(",")
                f.write(str(tuf[2]))
                f.write(",")
                f.write(str(tuf[3]))
                f.write(",")
                f.write(str(tuf[4]))
                f.write(",\n")
                
        cluster_no=cluster_no+1
    ax.ticklabel_format(useOffset=False, style='plain')
    plt.show()
