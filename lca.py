from collections import defaultdict
n = 8
edges = [
    [1, 2],
    [2, 3],
    [3, 4],
    [2, 5],
    [5, 6],
    [6, 7],
    [5, 8]
]
d = defaultdict(list)
for u,v in edges:
	d[u].append(v)
	d[v].append(u)
# print(d)
depth = [0] * (n + 1) 
parent = [0] * (n + 1)
def dfs(p ,node,k):
	parent[node] = p
	depth[node] = k
	for neigh in d[node]:
		if neigh != p:
			dfs(node,neigh,k + 1)
dfs(-1,1,0)
def lca(u,v):
	while depth[u] > depth[v]:
		u = parent[u]
	while depth[v] > depth[u]:
		v = parent[v]
	while u != v:
		u = parent[u]
		v = parent[v]
	return u
print(lca(7,8))
