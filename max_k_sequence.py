#max_k_sequence.py



def max_k_sum_sequence(data,k):
	dp=data[:]
	dp[k-1]=sum(data[0:k])
	maxresult=-65536
	for index in range(k,len(data)):
		dp[index]=dp[index-1]+data[index]-data[index-k]

		maxresult=max(maxresult, dp[index])

	return maxresult/k

print(max_k_sum_sequence([1,12,-5,-6,50,3], 2))