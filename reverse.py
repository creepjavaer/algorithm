#reverse.py

def ver(str,n):
	length=len(str)
	if n==0:
		return str
	elif n==length-1:
		return str[::-1]

	else:
		return str[-n:]+str[0:length-n]

def enhancerotate(str,offset):
	if not offset:
		return str
	if not str:
		return str

	n=len(str)
	offset%=n
	str=list(str)
	for i in range(offset):
		t=str.pop()
		str.insert(0,t)
	return "".join(str)

if __name__=="__main__":

	str="abcdefg"

	print(enhancerotate(str,0))
	print(enhancerotate(str,1))
	print(str)
	print(enhancerotate(str,1))
	



