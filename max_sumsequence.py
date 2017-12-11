#max_sumsequence.py

def max_sum_sequence(left,right):
	i=0
	j=0
	new=[]
	while i<len(left) and j<len(right):
		if left[i]<right[j]:
			new.append(left[i])
			i+=1
		elif left[i]>right[j]:
			new.append(right[j])
			j+=1
		else:
			new.append(left[i])
			i+=1
			j++1
	if i<len(left):
		new+=left[i:]
	else:
		new+=right[j:]  
		

	return new


if __name__=="__main__":
	arr=[1,2,3,4,5,6]
	a=[1,3,4,5,6,7]
	print(max_sum_sequence(arr,a))