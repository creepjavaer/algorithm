#hello.py
def maxsumsequence(array):
	thissum=0
	i=j=0
	maxsum=array[0]

	for index,item in enumerate(array):
		thissum+=item

		if thissum>maxsum:

			maxsum=thissum
			j=index 
		elif thissum<=0: 
			thissum=0
			#i=j

	cursum=maxsum

	i=j

	while  cursum:
		cursum-=array[i]
		i-=1
	


	return maxsum ,array[i+1:j+1]


def test():
	array0=[0,0,1,0,33333,-33333]
	print(maxsumsequence(array0))

test()