#max_sequence.py

def maxsequence(array):
	dp=array[:]
	maxcount=-65595
	for index in range(len(array)):
		if index>=1:
			if array[index]>array[index-1]:
				dp[index]=dp[index-1]+1
				maxcount=max(maxcount, dp[index])
			else:
				dp[index]=1

	return maxcount

if __name__ == "__main__":
	array=[0,0,0,5,2,3,4,1,-2,0,4,5,6,7,8]
	print(maxsequence(array))

