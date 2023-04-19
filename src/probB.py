import sys
import math
import heapq
input = sys.stdin.readline
#import io,os
#input = io.BytesIO(os.read(0,os.fstat(0).stsize)).readline
 
#n is the number of nodes
#m is the number of edges
#s is the source
#t is the target
n, m, s, t= map(int, input().split())
 
l = []
 
for i in range(m):
    a, b, w, c = list(map(int, input().split()))
    l.append((a, b, w, c))
if (len(l) == 0):
    a, b, w, c = [0,0,0,0]
else:
    a, b, w, c = zip(*l)




def shortestsnowy(n,m, s, t, a, b, w, c):
    if (s == t):
        return 0, 0
    if (m == 0):
        return -math.inf, -math.inf
    #adjList = {1: [arrivee, length, snow], 2: [arrivee, lenth]}

    #clearer with a dic

    graphSnow = {node: {} for node in range(n+1)}
    for i in range(m):
        graphSnow[a[i]][b[i]] = c[i]
        graphSnow[b[i]][a[i]] = c[i]
        
    #for key in graphSnow.keys():
    #    print(key, ":", graphSnow[key])
    
    #heapq.heappush(heapSnow, ((c[i], w[i], s, t)))
    #first modified dijkstra on snow (takes maximum instead of addition) (heap is of the form (node, snow))
    #modif graphSnow to only contain c[i] <= maximal_minimum_snow
    #run normal dijkstra on modified graphSnow (heap is of the form (node, length))

    opt_snow = dijkstraSnow(graphSnow, s, t)
    graphLen = {node: {} for node in range(n+1)}
    for i in range(m):
        if(c[i] > opt_snow):
            continue
        else:
            graphLen[a[i]][b[i]] = w[i]
            graphLen[b[i]][a[i]] = w[i]

    min_len = dijkstraLen(graphLen, s, t)
    return opt_snow, min_len

def dijkstraSnow(graph, start_vertex, end_vertex):
    snow_cover = {vertex: math.inf for vertex in graph}
    snow_cover[start_vertex] = 0

    pq = [(0, start_vertex)]
    while len(pq) > 0:
        current_snow, current_vertex = heapq.heappop(pq)

        if current_snow > snow_cover[current_vertex]:
            continue

        for neighbor, snow in graph[current_vertex].items():
            max_min_snow = max(current_snow, snow)

            if max_min_snow < snow_cover[neighbor]:
                snow_cover[neighbor] = max_min_snow
                heapq.heappush(pq, (max_min_snow, neighbor))

    return snow_cover[end_vertex]


def dijkstraLen(graph, start_vertex, end_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0

    pq = [(0, start_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    if distances[end_vertex] != math.inf:
        return distances[end_vertex]
    else:
        return -math.inf

snow, shortestLen = shortestsnowy(n, m, s, t, a, b ,w, c)

if (shortestLen == -math.inf):
    print("Impossible")
else:
    print(snow, shortestLen)




