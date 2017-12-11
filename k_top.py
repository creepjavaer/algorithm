#k_top.py
def partion(array,left,right):
	temp=array[0]
	i=left
	j=right
	while i!=j:
		while i <j and array[j]>=temp:
			j-=1
		while i <j and array[i]<=temp:
			i+=1

		if i!=j:
			array[i],array[j]=array[j],array[i]

	array[0]=array[i]
	array[i]=temp

	return i

def result(array,left,right,k):
	#i=-65536
	i=partion(array, left, right)
	g=len(array)-k
	while i!=g:
		if i<g:
			i=partion(array,i+1,right)

		elif i>g:
			i=partion(array,left, i-1)

	return array[i]

array=[0,3,5,-1,2,9,-3,10]

print (result(array,0,7,2))