#replace.py

def result(s):
	res=""

	for c in s:
		if c !=" ":
			res+=c
		else:
			res+="%20"
	return res
if __name__=="__main__":
	print(result("hello liuyan liyan hi j  "))


