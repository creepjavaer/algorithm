#unzip.py
def unzip(str):
	loopstr=""
	count=0
	result=""
	j=0
	total=len(str)
	number="0"
	i=0
	count=0
	while i <total:
		if str[i]=="[":
			#count=int(str[i-1])
			j=i+1
			while j <len(str) and str[j]!="]":
				loopstr+=str[j]
				j+=1
			count=int(number)
			while count:
				result+=loopstr
				count-=1


			if j==len(str):
				return str

			else:
				i=j+1
		elif str[i].isnumeric():
			number+=str[i]
			i+=1

		elif str[i]!="]" :
			result+=str[i]
			i+=1

	return result


print(unzip("ab5[hi]de"))
