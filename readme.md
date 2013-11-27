sharedGamut v0.1
====================

python module to calcualte shared gamut of n gamuts. 


### usage:

get Polygon library at https://pypi.python.org/pypi/Polygon 


create Polygon object with gamut data as vertices.
                         r(x, y)         g(x, y)         b(x, y) 
g1 = Polygon.Polygon(((0.651, 0.302), (0.196, 0.691), (0.145, 0.092)))

**pr1 = projector("192.168.0.8", 3002)**

*// get all Lamp data as Dictionary*

**print pr1.getLampInfo()**

*// get lamp hours data as integer*

**print pr1.getLampInfo()["LampHours"]**



*// get all temperature data as Dictionary*

**print pr1.getTemperatures()**

*// get red DMD temperature as integer*

**print pr1.getTemperatures()["red"]**

