#first.py

def first(l,n):
	datas=l[0:l.index(n)]
	d={}
	for data in datas:
		d[data]=0

	for data in datas:
		d[data]+=1

	first=100000
	for k,value in d.items():
		if value==1:
			first=min(first,datas.index(k))

	if first==100000:
		if n in datas:
			return datas[datas.index(n)]
		else:
			return -1
	else:
		return datas[first] 


	
print(first([1,2,3,2,1,5,6,7],5))