#te.py

d={1:2,3:9,6:9}
print(sorted(d.items(),key=lambda  a :a[1]))

print(d.items())
print(d)




def f(array):
	dp=array[:]
	begin=0
	end=0
	re=-65535
	for i in range(len(array)):
		if i>=1:
			if dp[i]^dp[i-1]>array[i]:
				dp[i]=dp[i]^dp[i-1]
				re=max(re, dp[i])
				end=i
			else:
				begin=i

	return array[begin:end],re



