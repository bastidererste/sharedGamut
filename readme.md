sharedGamut v0.1
====================

python module to calcualte shared gamut of n gamuts. 


### usage:

get Polygon library at https://pypi.python.org/pypi/Polygon 


create Polygon object with gamut data as vertices.

                         r(x, y)         g(x, y)         b(x, y) 

gn = Polygon.Polygon(((0.651, 0.302), (0.196, 0.691), (0.145, 0.092)))

get the intersection Polygon with the & operator

a = g1 & g2 & g3  

