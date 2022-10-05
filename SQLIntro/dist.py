#https://www.geeksforgeeks.org/program-distance-two-points-earth/#:~:text=For%20this%20divide%20the%20values,is%20the%20radius%20of%20Earth

import math

Latitude1 = 38.2053
Longitude1 = -87.4179
Latitude2 =  37.9678
Longitude2 = -87.4855

lat1 = Latitude1 / 57.29577951
long1 = Longitude1  / 57.29577951

lat2 = Latitude2 / 57.29577951
long2 = Longitude2  / 57.29577951

print (lat1, long2, lat2, long2)


d = 3963.0 * math.acos((math.sin(lat1) * math.sin(lat2)) + math.cos(lat1) * math.cos(lat2) * math.cos(long2 - long1))

print (d)