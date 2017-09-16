import math

R = 6371

def haversine(lat1,lat2,long1,long2):
    latint1 = math.radians(float(lat1))
    latint2 = math.radians(float(lat2))
    longint1 = math.radians(float(long1))
    longint2 = math.radians(float(long2))

    deltalat = latint2 - latint1
    deltalong = longint2 - longint1

    a = math.sin(deltalat/2) * math.sin(deltalat/2) + math.cos(latint1) * math.cos(latint2) * math.sin(deltalong/2) * math.sin(deltalong/2)
    c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))#latlongfile = open("latlong.txt","r")
    return 0.95*R*c

def makeheuristic():
    latlongfile = open("latlong.txt","r")
    for line in latlongfile.readlines():
        splitline = line.split(" ")
        name = splitline[0]
        lat = splitline[1]
        long = splitline[2]
        path = "cities/" + name + ".txt"
        datafile = open(path,"w")
        latlongfile2 = open("latlong2.txt","r")
        for line2 in latlongfile2.readlines():
            splitline2 = line2.split(" ")
            name2 = splitline2[0]
            lat2 = splitline2[1]
            long2 = splitline2[2]
            val = haversine(lat,lat2,long,long2)
            output = name2 + " " + str(val) + "\n"
            datafile.write(output)
        datafile.close()
    latlongfile.close()

makeheuristic()



    
    
    
