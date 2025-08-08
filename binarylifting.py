class BinaryLifting:
    def __init__(self, n, adj, root=0):
        self.n = n
        self.LOG = (n-1).bit_length()        
        self.up = [[-1]*n for _ in range(self.LOG)]
        self.depth = [0]*n
        self._dfs(root, parent=-1, adj=adj)
        for k in range(1, self.LOG):
            for v in range(n):
                prev_ancestor = self.up[k-1][v]
                self.up[k][v] = -1 if prev_ancestor < 0 else self.up[k-1][prev_ancestor]
                
    def _dfs(self, v, parent, adj):
        self.up[0][v] = parent
        for w in adj[v]:
            if w == parent:
                continue
            self.depth[w] = self.depth[v] + 1
            self._dfs(w, v, adj)

    def lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        diff = self.depth[u] - self.depth[v]
        for k in range(self.LOG):
            if diff & (1 << k):
                u = self.up[k][u]
        if u == v:
            return u
        for k in reversed(range(self.LOG)):
            if self.up[k][u] != self.up[k][v]:
                u = self.up[k][u]
                v = self.up[k][v]
        return self.up[0][u]
