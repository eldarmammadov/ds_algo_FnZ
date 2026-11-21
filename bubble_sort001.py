

def bubble(arr,sorted=[]):
	sorted = [None] * (len(arr))
	for k in range(len(arr)):
		try:
			if arr[k] > arr[k+1]:
				sorted[k] = arr[k]
				sorted[k+1] = arr[k+1]
				arr[k] = sorted[k+1]
				arr[k+1] = sorted[k]
		except:
			return arr
	return arr
	
	
bubble([2,1,3])


