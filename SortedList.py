from bisect import bisect_left as lower_bound
from bisect import bisect_right as upper_bound
class FenwickTree:
    def __init__(self, x):
        self.bit = list(x)
        self.size = len(self.bit)
        for i in range(self.size):
            j = i | (i + 1)
            if j < self.size:
                self.bit[j] += self.bit[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < self.size:
            self.bit[idx] += x
            idx |= idx + 1

    def __call__(self, end):
        """Calculates sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def find_kth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(self.size.bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < self.size and self.bit[right_idx] <= k:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1, k

class SortedList:
    block_size = 700

    def __init__(self, iterable=()):
        iterable = sorted(iterable)
        self.micros = [iterable[i:i + self.block_size - 1] for i in range(0, len(iterable), self.block_size - 1)] or [[]]
        self.macro = [block[0] for block in self.micros[1:]]
        self.micro_size = [len(block) for block in self.micros]
        self.fenwick = FenwickTree(self.micro_size)
        self.size = len(iterable)

    def append(self, x):
        i = lower_bound(self.macro, x)
        j = upper_bound(self.micros[i], x)
        self.micros[i].insert(j, x)
        self.size += 1
        self.micro_size[i] += 1
        self.fenwick.update(i, 1)
        if len(self.micros[i]) >= self.block_size:
            self.micros[i:i + 1] = [self.micros[i][:self.block_size >> 1], self.micros[i][self.block_size >> 1:]]
            self.micro_size[i:i + 1] = [self.block_size >> 1, self.block_size >> 1]
            self.fenwick = FenwickTree(self.micro_size)
            self.macro.insert(i, self.micros[i + 1][0])

    def pop(self, k=-1):
        i, j = self._find_kth(k)
        self.size -= 1
        self.micro_size[i] -= 1
        self.fenwick.update(i, -1)
        return self.micros[i].pop(j)

    def __getitem__(self, k):
        i, j = self._find_kth(k)
        return self.micros[i][j]

    def count(self, x):
        return self.upper_bound(x) - self.lower_bound(x)

    def __contains__(self, x):
        return self.count(x) > 0

    def lower_bound(self, x):
        i = lower_bound(self.macro, x)
        return self.fenwick(i) + lower_bound(self.micros[i], x)

    def upper_bound(self, x):
        i = upper_bound(self.macro, x)
        return self.fenwick(i) + upper_bound(self.micros[i], x)

    def _find_kth(self, k):
        return self.fenwick.find_kth(k + self.size if k < 0 else k)

    def __len__(self):
        return self.size

    def __iter__(self):
        return (x for block in self.micros for x in block)

    def __repr__(self):
        return str(list(self))


