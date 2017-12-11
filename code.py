#code.py
def result(string):
	code=dict(zip("abcdefghijklmnopqrstuvwxyz",list(range(0,25))))
	print(code)
	s=sorted(string)
	res=0
	dp=[code[i] for i in s]
	#dp.append(object)
	i=1
	while i <len(s):
		if s[i]==s[i-1]:
			dp[i]=dp[i-1]+1
		else:
			dp[i]=dp[i-1]+code[s[i]]

		i+=1
	return dp.pop()

print(result("aab"))

