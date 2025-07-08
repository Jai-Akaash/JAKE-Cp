class rollHash:
    def _init_(self,s):
        self.s = s
        self.mod = 10 ** 9 + 7
        self.base = 257
        self.n = len(s)
        self.pre = [0] * (self.n + 1)
        self.pow = [1] * (self.n + 1)
        self.precompute()
    def precompute(self):
        for i in range(1,self.n + 1):
            self.pre[i] = (self.pre[i - 1] * self.base + self.s[i - 1]) % self.mod
            self.pow[i] = (self.pow[i - 1] * self.base) % self.mod
    def get(self,l,r):
        return (self.pre[r] - self.pre[l] * self.pow[r - l]) % self.mod
