class segTree:
	def __init__(self,n,arr):
		self.n = n
		self.tree = [0] * (4 * self.n)
		self.build(1,0,self.n - 1,arr)
	def build(self,node,start,end,arr):
		if start == end:
			self.tree[node] = arr[start]
			return 
		mid = (start + end) // 2
		self.build(2 * node,start,mid,arr)
		self.build(2 * node + 1,mid + 1,end,arr)
		self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]
	def update(self,node,start,end,idx,val):
		if start == end:
			self.tree[node] = val
			return 
		mid = (start + end) // 2
		if idx <= mid:
			self.update(2 * node,start,mid,idx,val)
		else:
			self.update(2 * node + 1,mid + 1,end,idx,val)
		self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]
	def query(self,node,start,end,L,R):
		if start > R or end < L:
			return 0
		if start >= L and end <= R:
			return self.tree[node]
		mid = (start + end) // 2
		return self.query(2 * node,start,mid,L,R) + self.query(2 * node + 1,mid + 1,end,L,R)

arr = [2,5,4,1]
st = segTree(len(arr),arr)
print(st.tree[1])
st.update(1,0,len(arr) - 1,3,5)
print(st.tree[1])
print(st.query(1,0,len(arr) - 1,1,3))
