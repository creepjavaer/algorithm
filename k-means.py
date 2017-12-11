#k-means.py
#@ pumpkin 2017-10-5

import matplotlib.pyplot  as plt
import random
import math
import copy
# define the data which we use to implement the k-means  algorithm
# x,y is limitted to between [0,50]
class Point():
	def __init__(self,x,y):
		
		self.x=x
		self.y=y

def showdatas(datas):
	x_values=[]
	y_values=[]
	
	for point in datas:
		x_values.append(point.x)
		y_values.append(point.y)

	plt.scatter(x_values,y_values,s=10)
	#plt.axis=([0,100,300,500])
	#print(len(x_values))
	plt.show()

def showresult(result):	
	index=[[],[],[],[],[],[],[],[]]
	
	i=0
	j=1
	count=0
	color=["red","black","purple","green"]
	
	for key ,points in result.items():
		index[i].append (key.x)
		index[j].append(key.y)
		
		if points :
			for point in points:	
				#x_values.append(point.x)
				index[i].append(point.x)
				index[j].append(point.y)

		plt.scatter(index[i], index[j],c=color[count])

		plt.scatter(index[i][0], index[j][0] ,c=color[count],s=100 )
		count+=1

		i+=2
		j+=2

	
	plt.show()


def create_data(n):
	datas=[]

	while n:
		p=Point(random.randint(0,10),random.randint(5, 30))
		datas.append(p)
		n-=1
	return datas

def distance_two_point(point1,point2):
	return math.sqrt(pow(point1.x-point2.x,2)+pow(point1.y-point2.y,2))


def k_means(k,datas):

	n=len(datas)-1
	dis={}
	index=[]
	index.append(random.randint(0,n-1))
	for num in range(k):
		while True:
			s=random.randint(0,n-1)
			if s not in index:
				index.append(s)
				break
		
		dis[copy.deepcopy(datas[s])]=[]
		
	change=True
	total=1000

	while change :
		change=False
		total-=1
		#temp_clusetr=None

		for data in datas:
			minsdia=65535600
			temp_clusetr=None

			for center_clusetr_in_dis in dis.keys():
				#temp_clusetr=center_clusetr_in_dis
				#if data.x !=center_clusetr_in_dis.x and data.y !=center_clusetr_in_dis.y:
				
					temp=distance_two_point(data,center_clusetr_in_dis)
					if temp<minsdia:
						minsdia=temp
						temp_clusetr=center_clusetr_in_dis

			dis[temp_clusetr].append(data)
			
		count =0
		for key in dis.keys():
			points=dis[key]
			addx=0
			addy=0
			lenth=len(points)
			
			for point in points:
				addx+=point.x
				addy+=point.y

			point=Point(addx/lenth,addy/lenth)
			#key.x=addx/2
			#key.y=addy/2

			if distance_two_point(point,key)<0.000001:
				count+=1	
			else:
				change=True

			key.x=point.x
			key.y=point.y

		if count == k:
			#result.append(dis)
			print("finish in 收敛")
			return dis 
		elif not total:
			#result.append(dis)
			print("meiyou shoulian")
			return dis 
		
		else:
			for key in dis.keys():
				dis[key].clear()
								
	return dis

datas=create_data(50)
showdatas(datas)
dis=k_means(4,datas)
#print("hahah")
showresult(dis)
#print(len(result))
#showdatas(datas)





 







	















		

	













	





