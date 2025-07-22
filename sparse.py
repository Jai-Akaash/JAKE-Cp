class sparse:
	def __init__(self,arr,func):
		self.func = func
		self.n = len(arr)
		self.maxik = math.floor(math.log2(self.n))
		self.sp = [[0] * self.n for _ in range(self.maxik + 1)]
		self.sp[0] = arr.copy()
		for k in range(1,self.maxik + 1):
			length = 2 ** k 
			half = 2 ** (k - 1)
			for i in range(self.n - length + 1):
				self.sp[k][i] = func(self.sp[k - 1][i],self.sp[k - 1][i + half])
	def query(self,l,r):
		length = r - l + 1
		k = math.floor(math.log2(length))
		half = 2 ** k 
		return self.func(self.sp[k][l] ,self.sp[k][r - half + 1])

