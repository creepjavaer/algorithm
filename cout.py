def result(string):
	i=1
	count=1
	sum=0
	new=1
	if not string:
		return 

	if len(string)==1:
		return 1

	while i < len(string):
		if string[i]==string[i-1]:
			count+=1
			#sum+=count

		else:
			sum+=count
			new+=1
			count=1
			#sum+=count

		i+=1

	if  count==len(string):
		return len(string)

	sum+=count

	return  sum,new,sum/new


if __name__=="__main__":
	print(result("aaabbc")