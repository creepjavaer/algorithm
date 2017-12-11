#merge_sort.py
def quick_sort(lists,left,right):
	if left>=right:
		return lists
	print("heheh")
	key=lists[left]
	low=left
	high=right

	while left<right:
		while left<right and lists[right]>=key:
			right-=1

		lists[left]=lists[right]
		while left<right and lists[left]<=key:
			left+=1

		lists[right]=lists[left]
	lists[right]=key
	quick_sort(lists,low,left-1)
	print("hahhah")
	quick_sort(lists,left+1,high)
	return lists

print(quick_sort([1,2,-3,4,6,7-1,5,8],0,8)) 
