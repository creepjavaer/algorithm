#onepoint.py

def result(array):
	lenth=len(array)
	i=1
	while i<=lenth-2:
		if array[i]>arr[i-1] and array[i]>arr[i+1]:
			if array[i+1]>array[i-1]:
				return True
		i+=1
	return False


if __name__=="__main__":
	arr=[3,1,4,2]

	print(result(arr))
