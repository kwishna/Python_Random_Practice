class BoundedIterator():
	'''
		@author Krishna
		This Class Represent How A Class Can Implement Iterator.
	'''
	def __init__(self, value, boundCount):
		self.value = value
		self.boundCount = boundCount
		self.count = 0
		
	def __iter__(self):
		return self
	
	def __next__(self):
	
		if self.count >= self.boundCount:
			raise StopIteration
		
		else:
			self.count += 1
			return self.value
			
	# Python 2 compatibility. Since, __next__ Is The Changed Name For Py3.
    def next(self):
        return self.__next__()
		
			
if __name__ == "__main__":
	
	b1 = BoundedIterator(5, 3)
	for i in b1:
		print(i)
		
	
	b2 = BoundedIterator(10, 5)
	itr2 = iter(b2)
	while True:
		try:
			print(next(itr2))
		except:
			'''
				print('StopIteration')
			'''
			break
	