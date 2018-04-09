## Как итерировать числа от 1 до 10000?
Итерировать числа от 1 до 10000 можно несколькими способами:
1. range(xrange)
	```python
	v1 = range(1, 10000) # Python3
	v2 = xrange(1, 10000) # Python2
	```
2. class
	```python
	class IterThousand(object):
		def __init__(self):
			self.i = 0
		def __iter__(self):
			return self
		def __next__(self):
			self.i += 1
			if self.i < 10000:
				return self.i
			raise StopIteration
	```
