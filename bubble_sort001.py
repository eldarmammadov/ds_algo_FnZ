

def bubble(arr,sorted=[]):
	sorted = [None] * (len(arr))
	unsorted = True
	while unsorted:
		for k in range(len(arr)):
			print(k)
			try:
				unsorted = False
				if k != len(arr)+1 and arr[k] >= arr[k+1]:
					unsorted = True
					sorted[k] = arr[k]
					sorted[k+1] = arr[k+1]
					arr[k] = sorted[k+1]
					arr[k+1] = sorted[k]
					print(arr)
			except:
				print('error')
				bubble(arr)
	return arr
	


list = [4,3,2,1]
bubble([2,1,3])


