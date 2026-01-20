class DSU :
    def _init_(self, n) :
        self.parent = [i for i in range(n + 1)]
        self.size = [1 for i in range(n + 1)]
        self.rank = [0 for i in range(n + 1)]

    def FindUParent(self, node) :
        if (node == self.parent[node]) :
            return node
        self.parent[node] = self.FindUParent(self.parent[node])
        return self.parent[node]

    def UnionByRank(self, u, v) :
        Upu = self.FindUParent(u)
        Upv = self.FindUParent(v)
        if (Upu == Upv) :
            return 
        if (self.rank[Upu] == self.rank[Upv]) :
            self.parent[Upv] = Upu 
            self.rank[Upu] += 1
        elif (self.rank[Upu] < self.rank[Upv]) :
            self.parent[Upu] = Upv 
        else :
            self.parent[Upv] = Upu 

    def UnionBySize(self, u, v) :
        Upu = self.FindUParent(u)
        Upv = self.FindUParent(v)
        if (Upu == Upv) :
            return 
        if (self.size[Upu] < self.size[Upv]) :
            self.parent[Upu] = Upv 
            self.size[Upv] += self.size[Upu]
        elif (self.size[Upv] <= self.size[Upu]) :
            self.parent[Upv] = Upu 
            self.size[Upu] += self.size[Upv]

