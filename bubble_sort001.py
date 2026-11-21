

def bubble(arr,sorted=[]):
"""Happens Kisa Principle forged to make to happen to sort a list, but manual shifting for passover's"""
	sorted = [None] * (len(arr))
	for k in range(len(arr)):
		try:
			if arr[k] > arr[k+1]:
				first = arr[k]
				lesser = arr[k+1]
				arr[k] = lesser
				arr[k+1] = first
		except:
			return arr
	return arr
	
	
bubble([2,1,3])


