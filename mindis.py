#mindis.py
def mincopy(source , des):
	i=0
	j=1
	minstr=""
	count=0
	minlen=2579
	sourcehash=dict(zip(source, [0*i for i in range(len(source))]))
	print(sourcehash)
	sourcehash[source[0]]=1

	if source[0] in des:
		count +=1
		#minstr+=source[0]
	#dict(zip(source, [0*i for i in range(257)]))
	#for char in source :
		#sourcehash[char]+=1
	while i<j and j<len(source):
		#sourcehash[source[j]]+=1
		if not sourcehash[source[j]] and source[j] in des:
			count+=1
		sourcehash[source[j]]+=1

		if count==len(des):
			sourcehash[source[i]]-=1
			if source[i] in des and not sourcehash[source[i]]:
				count-=1
			i+=1
		else:
			j+=1	
	print(i,j)

if __name__=="__main__":
	source="adobecodebanc"
	des="abc"

	print(mincopy(source, des))




	
