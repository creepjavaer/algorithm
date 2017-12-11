#test.py

class d (dict):
	def __set__(self,key,value):
		self[key]=value
	def __init__(self,**kw):
		super(d,self).__init__(**kw)
a=d(f=1,b=2,c=3)
a.__set__("1",2)
print(a)