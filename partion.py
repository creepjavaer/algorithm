#partion.py
def partion(array,data):
	low =0
	high=len(array)-1

	while low <high:
		while low <high and array[high]>=data:
			high-=1

		while low <high and array[low]<data:
			







