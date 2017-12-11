#serchstr.py

def search(str1,str2):
	i=0
	j=0
	len1=len(str1)
	len2=len(str2)
	while i<len1 and j<len2:
		if str1[i]==str2[j]:
			i+=1
			j+=1
			if j==len2-1:
				return True

		else:
			i+=1
			j=0

	return False


print(search("hello", "helllll"))