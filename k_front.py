#k_front.py
import math

def result(array,orign):
	d={}
	for point in array:
		dist=dis(point, orign)
		d[point]=dist
	return d

def dis (orign,tup):
	return math.sqrt(pow(orign[0]-tup[0],2)+pow(orign[1]-tup[1],2))


orign=(0,0)
array=[(4,6),(4,7),(4,4),(2,5),(1,1)]

d=result(array, orign)
re=sorted(d.items(),key=lambda e:e[1])


r=[]
for i in range(3):
	r.append(re[i][0])
print(r)
