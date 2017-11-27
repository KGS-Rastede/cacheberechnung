from geopy.distance import *



#unbekannt ist x und z
s=111
t=111
u=111
v=111
w=111
y=111


# Stadtzentrum Oldenburg
innenstadt = Point(53.08400, 8.12800)



koordinaten = []

for x in range(100,105):
    for z in range(200,201):
        n = 3*(s+t+u+v)+w+x+441
        e = 9*(z+y+x+w)-v-u-881
        
        N = "53."+str(n)
        E = "8."+str(e)
        
        
        neue_koordinate = Point(N, E)
        
        koordinaten.append(neue_koordinate)

for k in koordinaten:
    #print(k)
    print(innenstadt)
    #print(vincenty(k, innenstadt).km)
        

# N 53° 3*(S+T+U+V) +W+X+441
# E 008° 9*(Z+Y+X+W) -V-U-811

