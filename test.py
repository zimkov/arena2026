
from arena_sdk import *

drone = Pioneer("pioneer1")
rts = Geobot("geobot1")
print(type(drone))
print(type(rts))

if type(drone) is Pioneer:
    print(type(drone) is Pioneer)
if type(rts) is Geobot:
    print(type(rts) is Geobot)
