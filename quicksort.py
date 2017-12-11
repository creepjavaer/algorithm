#quicksort.py

def partion(array,begin,end):
	
    pivotIndex=bigin
    pivot=array[pivotIndex]
    array[pivotIndex],array[end]=array[pivotIndex],array[end]
    low=begin
    high=end

    
	

def quicksort(array,begin,end):
	if begin <end :
		par=partion(array,begin,end)
		quicksort(array, begin, par-1)
		quicksort(array,par+1,end)

array=[1-1,3,5.-8,-4,9,10]

quicksort(array, 0, len(array)-1)

print(array)

		

