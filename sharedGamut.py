import Polygon
import math

//                       r(x, y)         g(x, y)         b(x, y) 
g1 = Polygon.Polygon(((0.651, 0.302), (0.196, 0.691), (0.145, 0.092)))
g2 = Polygon.Polygon(((0.626, 0.332), (0.216, 0.711), (0.162, 0.058)))
g3 = Polygon.Polygon(((0.571, 0.322), (0.167, 0.646), (0.191, 0.044)))
a = g1 & g2 & g3 // & = intersection 


redDist[]; //will contain all distances from every a(x, y) to r(1,0)
greenDis[]; //will contain all distances from every a(x, y) to g(0,1)
blueDist[]; //will contain all distances from every a(x, y) to b(0,0)

for point in a[0]:
	redDist.append(math.sqrt((1-point[0])**2+(0-point[1])**2))
	greenDist.append(math.sqrt((0-point[0])**2+(1-point[1])**2))
	blueDist.append(math.sqrt((0-point[0])**2+(0-point[1])**2))

redRefx = a[0][redDist.index(min(redDist))][0]
redRefy = a[0][redDist.index(min(redDist))][1]
greenRefx = a[0][greenDist.index(min(greenDist))][0]
greenRefy = a[0][greenDist.index(min(greenDist))][1]
blueRefx = a[0][blueDist.index(min(blueDist))][0]
blueRefy = a[0][blueDist.index(min(blueDist))][1]
