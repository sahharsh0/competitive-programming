'''
microservice pipeline development
consider a cloud native software system composed of V autonomous microservices indexed 0 through V-1
the initializatin graph  is defined by directed dependency constraints [u,v] mandating that
service v must complete execution before service u begins
construct a graph theoretic topological sorting routine based on the Kahn's algorithm to determine a valid linear 
boot sequence, or detect cyclic inter dependencies prevent the launch
input:
num_modules=4, prerequisities=[[1,0],[2,0],[3,1],[3,2]]
output:
valid microservice build order = 0,1,2,3
'''
from collections import deque
def findBuildOrder(num_modules, prerequisites):
    graph = [[] for _ in range(num_modules)]
    indegree = [0] * num_modules
    for u, v in prerequisites:
        graph[v].append(u)
        indegree[u] += 1
    queue = deque()
    for i in range(num_modules):
        if indegree[i] == 0:
            queue.append(i)
    order = []
    while queue:
        current = queue.popleft()
        order.append(current)
        for next_module in graph[current]:
            indegree[next_module] -= 1
            if indegree[next_module] == 0:
                queue.append(next_module)
    if len(order) != num_modules:
        return "Cycle detected - no valid build order"
    return order
num_modules = 4
prerequisites = [ [1, 0], [2, 0], [3, 1], [3, 2]]
print("Valid microservice build order =", findBuildOrder( num_modules, prerequisites))