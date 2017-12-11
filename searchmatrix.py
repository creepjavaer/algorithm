#searchmatrix.py

def search(array,data):
	i=0 #第0行
	j=len(array[0])-1 #最后一行
	while i<=2 and j>=0:
		if array[i][j]<data: 
			i+=1
		elif array[i][j]>data:
			j-=1
			
		else :
			return i,j 
			
	return -1

array=[[1,3,5,7],[10,11,16,20],[23,30,34,50]]

print(search(array, 20))