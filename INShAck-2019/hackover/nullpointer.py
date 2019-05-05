with open( 'routes.txt', 'r') as f:
   data=f.read().splitlines()
tap=[]
while len(data) > 0:
    print( "There are %d routes"%len(data))
    conn_stat = {}
    conn_route = {}
    conn_nr_route={}
    i=0
    for datum in data:
        #print("Analysis of %s"%datum)
        connections=datum.split(',')
        for connection in connections:
            if len(connection) < 5:
                continue
            #if connection == "e5a10f35":
            #    print(datum)
            #print(connection)
            if connection not in conn_stat:
                conn_stat[connection]=1
                conn_route[connection]=[]
                conn_nr_route[connection]=0
            else:
                #print("Extend")
                conn_stat[connection]=conn_stat[connection]+1
            if datum not in conn_route[connection]:
                conn_route[connection].append( datum )
                conn_nr_route[connection] = conn_nr_route[connection] + len( connections )
                #conn_route[connection].append( i )
        i=i+1
    w=0
    d=None
    n = 0
    for k in conn_stat.keys():
        if w < conn_stat[k] or d == None:
            if d == None or conn_nr_route[k] > conn_nr_route[d]:
                d=k
                w=conn_stat[k]
    print( "Best tap point is %s and it lead to remove %d routes"% (d, len(conn_route[d])) )
    #print( conn_route[d] )
    tap.append(d)
    #print( "Current tap list is ", tap)
    for k in conn_route[d]:
        data.remove(k)
print( "Finished with %d"%len(tap))
for t in tap:
    print(t)
