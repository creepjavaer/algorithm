#text.py

#def swap(a,b):

	#a,b=b,a
	#return a,b

#print(swap(1, 2))

def swap(array):
	array[0],array[1]=array[1],array[0]

array=[1,2,3,4]

swap(array)

print(array)
for i in range(10):
	if i==3:
		i=5

	print(i)

l=["abcdef","defmn"]
s=l[0]
print(s)

dp=[100]
print(dp[0])
len(dp)
l.remove(s)
print(l.index("defmn"))


print("2".isnumeric())