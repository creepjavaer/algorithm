#buzz.py

def Buzz(n):
	result=[]
	for i in range(1,n+1):
		if i%3==0 and i%5==0:
			result.append("fizz buzz")
		elif i%3==0:
			result.append("fizz")
		elif i%5 ==0:
			result.append("buzz")

		else:
			result.append(str(i))

	return result



print(Buzz(15))