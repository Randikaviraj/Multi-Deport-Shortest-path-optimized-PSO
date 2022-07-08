import geopy.distance


def printknapSack(W, wt, val, n,names):
	K = [[0 for w in range(W + 1)] for i in range(n + 1)]
			
	for i in range(n + 1):
		for w in range(W + 1):
			if i == 0 or w == 0:
				K[i][w] = 0
			elif wt[i - 1] <= w:
				K[i][w] = max(val[i - 1]+ K[i - 1][w - wt[i - 1]],K[i - 1][w])
			else:
				K[i][w] = K[i - 1][w]

	
	res = K[n][W]
	print(res)
	
	w = W
	for i in range(n, 0, -1):
		if res <= 0:
			break
		if res == K[i - 1][w]:
			continue
		else:
			print(wt[i - 1])
			res = res - val[i - 1]
			w = w - wt[i - 1]



def findRoutes(values,weight,centroid):
    val =[]
    wt = []
    names=[]
    for ele in values:
        val.append(1/(geopy.distance.geodesic((ele[1],ele[2]),(centroid[0],centroid[1])).km))
        wt.append(int(ele[4]))
        names.append(ele[0])
    n = len(val)
    print(wt)
    print(val)
    printknapSack(weight, wt, val, n,names)

 