'''
A connected weighted graph represents cities and roads, 
you may add one new road of weight with btw any 2 previously connected cities
find where the node should be added to minimize the graphs routing diameter 
'''
def fbr(graph, weight):
    cities = list(graph.keys())
    n = len(cities)
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u in graph:
        for v, w in graph[u]:
            i = cities.index(u)
            j = cities.index(v)
            dist[i][j] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
    bd = float('inf')
    br = None
    for u in range(n):
        for v in range(u + 1, n):
            new_diameter = 0
            for a in range(n):
                for b in range(n):
                    old_distance = dist[a][b]
                    path1 = (dist[a][u]+ weight+ dist[v][b])
                    path2 = (dist[a][v]+ weight+ dist[u][b])
                    new_distance = min(old_distance, path1, path2)
                    new_diameter = max(new_diameter,new_distance)
            if new_diameter < bd:
                bd = new_diameter
                br = (cities[u], cities[v])
    return br, bd
print(fbr({'A': [('B', 1), ('C', 2)],'B': [('A', 1), ('C', 3)],'C': [('A', 2), ('B', 3)]}, 1))