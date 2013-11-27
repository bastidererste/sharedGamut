sharedGamut v0.1
====================

python module to calcualte shared gamut of n gamuts. 


### usage:

get Polygon library at https://pypi.python.org/pypi/Polygon 


create Polygon object with gamut data as vertices.

                         r(x, y)         g(x, y)         b(x, y) 

gn = Polygon.Polygon(((0.651, 0.302), (0.196, 0.691), (0.145, 0.092)))

get the intersection Polygon with the & operator

a = g1 & g2 & g3 & gn

calculate distances from every vertex in a to reference chromaticity r(1,0), g(0,1) and b(0,0)

for point in a[0]:
  
choose vertex with least distance to r(0,1) as redRef(x,y), to g(1,0) as greenRef(x,y) and to blueRef(x,y) to b(0,0)

redRefx = a[0][redDist.index(min(redDist))][0]

