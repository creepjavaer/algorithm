#serchber.py
def step(array,half,n):
	while array[half]==n and half:
		half-=1
	half+=1
	return half

def half_search(array,n):
	low=0
	high=len(array)-1
	while low <=high:
		half=low+high//2
		if array[half]==n:
			half=step(array, half, n)
			return half
		elif array[half]>n:
			high=half-1
		else:
			low=half+1
	
	return -1
