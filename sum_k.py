#sum_k.py
import math
def result(n,m):
	res=n
	if n==1:
		return res
		
	for index in range(1,m):
		res+=math.sqrt(n)
		n=math.sqrt(n)

	return res

print(result(100,2))
