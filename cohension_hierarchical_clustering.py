#cohension_hierarchical_clustering.py
import random
import math
import matplotlib.pyplot  as plt

class Point():
	def __init__(self,x,y):
		
		self.x=x
		self.y=y

class cluster(object):
	id=0
	"""docstring for ClassName"""
	def __init__(self, left=None,right=None):
		#super(ClassName, self).__init__()
		self.id+=1
		self.left=left
		self.right=right
		self.data=[]
		self.data.append(left)
		self.data.append(right)
		self.data+=left.data
		self.data+=right.data

	


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

def create_data(n):
	datas=[]

	while n:
		p=Point(random.randint(0,10),random.randint(5, 30))
		datas.append(p)
		n-=1
	return datas

def distance_two_list(point1,point2):
	mindist=655356
	data1=point1.data
	data2=point2.data
	print("appapapap")
	l=data1+data2
	#mindist=655356
	lens=len(l)-1

	for data1 in l:
		for data2 in l:
			if not data1==data2 :
				dis=distance_two_point(datas1, datas2)
				if dis<mindist:
					mindist=dis

	return mindist


def distance_two_point(point1,point2):
	return math.sqrt(pow(point1.x-point2.x,2)+pow(point1.y-point2.y,2))

def distance_two_difference(point,cluster):
	mindist=655356
	datas=cluster.data
	for data in datas:
		dis=distance_two_point(data, point)
		if dis<mindist:
			mindist=dis

	return mindist


def cohension_cluster(datas):

	while len(datas)>1:
		mindist=65535690
		index=None
		begin=None

		for data1 in datas:
			for data2 in datas:
				if not data1 is data2 and datas.index(data1)<datas.index(data2):

					if isinstance(data1, Point) and isinstance(data2,Point):
						dis=distance_two_point(data1, data2)
						print("ahhha")
					if isinstance(data1,cluster) and isinstance(data2, custer):
						print("xixixi")
						dis=distance_two_list(data1, data2)
					if isinstance(data1, Point) and isinstance(data2, cluster):
						print("heiheeihei")
						dis=distance_two_difference(data1, data2)

					if dis<mindist:
							mindist=dis
							end=data2
							begin=data1
							
		newcluster=cluster(begin,end)
		print(datas)
		datas.remove(begin)
		datas.remove(end)
		datas.append(newcluster.data)
	return datas

datas=create_data(5)
cohension_cluster(datas)
print(datas)







