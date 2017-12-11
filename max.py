#max.py
def maxmath(str):
	dp =[int(c) for c in str]
	for  i in range(len(str)):
		if i>=1:
			dp[i]=max(dp[i-1]*int(str[i]),dp[i-1]+int(str[i]))
	sum2=dp.pop()
	print(dp)
	return sum2

str="01104123"

print(maxmath(str))



