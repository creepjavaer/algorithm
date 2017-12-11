#merge.py
def merge(a,b):
	c=[]
	h=j=0

	while j<len(a) and h<len(b):
		if a[j]<b[h]:
			c.append(a[j])

			j+=1
		else:
			c.append(b[h])
			h+=1


	if j==len(a):
		c+=b[h:]

	else :
		c+=a[j:]

	return c
i=0
def sor(lists):
	global i
	i+=1
	if len(lists)<=1:
		return lists

	middle=len(lists)//2
	print(i)
	print("diicidiaoyong")

	left=sor(lists[:middle])
	print("hahah")
	print(left)
	right=sor(lists[middle:])
	print("******")
	return merge(left, right)



print(sor([4,7,8,3,5]))


