class GeneratorPy():
	
	def __init__(self):
		pass
	
	def repeater(self, val): # Infinite Generator
		while True: # Iterating Forever. If We Want It To Iterator For A Certain Time Then We Will Have To Put A Constraint. 
			yield self.val # Yield Mean Temporarily Return The State Of The Function.
			
	def bounded_repeater(self, value, max_repeats): # Limited Generator
		count = 0
		while True:
			if count >= max_repeats:
				return
			count += 1
			yield value
		
if __name__ == "__main__":
	g = GeneratorPy()
	#for i in g.repeater(5):
	#	print(i)
			
	for i in g.bounded_repeater('A', 5):
		print(i)		
		

		
#	>>> g = GeneratorPy(5)
#	>>> g.repeater(5)
#	<generator object GeneratorPy.repeater at 0x000001E890AFCB48>
	