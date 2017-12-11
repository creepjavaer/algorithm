#pca.py
import numpy as np
import csv

def loaddata(string):
	dataset=[]
	i=0
	j=0
	with open(string) as cs:
		reader=csv.reader(cs)
		for item in reader:
			i+=1
			if i!=1:
				while j<len(item):
					item[j]=int(item[j])
				dataset.append(item)

	print(np.array(dataset))
	return np.array(dataset)


def zeroMean(dataset):
	zerodata=np.mean(dataset,axis=0)
	dataset=dataset-zerodata
	return dataset,zerodata

def percentage2n(eigVals,percentage):
	sortArray=np.sort(eigVals)
	sortArray=sortArray[-1::-1]
	arraySum=sum(sortArray)

	tmpsum=0
	num=0

	for i in sortArray:
		tmpsum+=i
		num+=1
		if tmpsum>=arraySum*percentage:
			return num

def pca(dataMat,percentage=0.99): 
    newData,meanVal=zeroMean(dataMat)  
    covMat=np.cov(newData,rowvar=0)    #求协方差矩阵,return ndarray；若rowvar非0，一列代表一个样本，为0，一行代表一个样本  
    eigVals,eigVects=np.linalg.eig(np.mat(covMat))#求特征值和特征向量,特征向量是按列放的，即一列代表一个特征向量  
    n=percentage2n(eigVals,percentage)                 #要达到percent的方差百分比，需要前n个特征向量  
    eigValIndice=np.argsort(eigVals)            #对特征值从小到大排序  
    n_eigValIndice=eigValIndice[-1:-(n+1):-1]   #最大的n个特征值的下标  
    n_eigVect=eigVects[:,n_eigValIndice]        #最大的n个特征值对应的特征向量  
    lowDDataMat=newData*n_eigVect               #低维特征空间的数据  
    reconMat=(lowDDataMat*n_eigVect.T)+meanVal
    #重构数据  
    return lowDDataMat#,reconMat

print(pca(np.array([(1,2,3,4),(4,5,7,8),(7,8,9,10),(1,3,4,5),(1,0,1,1)])))

print(pca(np.array([(1,2,3,4,5,7,1,2,9,0),(1,2,4,3,5,6,8,9,1,4),
	(4,5,6,7,8,9,10,2,1,4),(2,2,3,4,5,6,7,7,8,1),
	(1,1,2,2,3,4,5,6,9,10),(2,4,6,8,10,12,30,10,3,10),
	(6,6,7,6,8,5,3,2,5,5),
	(1,1,1,3,5,2,1,3,5,10),(10,10,17,15,14,14,4,2,3,10),
	(1,1,1,2,3,4,5,2,3,10),(4,2,3,4,5,6,7,1,2,3)])))

print(pca(np.array([(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)])))