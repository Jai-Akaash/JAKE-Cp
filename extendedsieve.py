#JAKE#
from collections import defaultdict
def primeFact(n):
            d = defaultdict(set)
            spf = [i for i in range(n + 1)]
            p = 2
            while p * p <= n:
                if spf[p] == p:
                    for i in range(p * p,n + 1,p):
                        if spf[i] == i:
                            spf[i] = p
                p += 1
            d[1].add(1)
            for i in range(2,n + 1):
                j = i 
                while j != 1:
                    d[i].add(spf[j])
                    j = j // spf[j]
            return d 
print(primeFact(int(10e5)))