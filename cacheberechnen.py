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
temp_koordinaten = []

min_n = 10000000
min_e = 10000000

max_n = 1
max_e = 1

for x in range(100,999):
    for z in range(100,999):
        n = 3*(s+t+u+v)+w+x+441
        e = 9*(z+y+x+w)-v-u-881
        
        if e > max_e:
            max_e = e
            print("Neues max_e: "+str(max_e))
            
            
        if n > max_n:
            max_n = n
            print("Neues max_n: "+str(max_n))
            
        if e < min_e:
            min_e = e
            print("Neues min_e: "+str(min_e))
            
        if n < min_n:
            min_n = n
            print("Neues min_n: "+str(min_n))
            

        
        N = "53."+str(n)
        E = "8."+str(e)
        
        #print("N"+N+ " E"+ E)
        
        neue_koordinate = Point(N, E)
        
        temp_koordinaten.append(neue_koordinate)

print("\nMin/Max")

print("Osten geht von...bis")
print(min_e)
print(max_e)

print("Norden geht von...bis")
print(min_n)
print(max_n)


#

#print("\n Jetzt filtern\n")        
 
# Gefiltert
#print(len(temp_koordinaten))

#for i in temp_koordinaten:
#    if i not in koordinaten:
#        koordinaten.append(i)

# Ungefiltert               
#print(len(koordinaten))
 

#for k in koordinaten:
#    #print(k)
#    print(innenstadt)
#    #print(vincenty(k, innenstadt).km)
        

# N 53° 3*(S+T+U+V) +W+X+441
# E 008° 9*(Z+Y+X+W) -V-U-811

