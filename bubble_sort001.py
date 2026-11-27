

def bubble(arr,sorted=[]):
	sorted = [None] * (len(arr))
	unsorted = True
	counter = 0
	length = len(arr)
	while unsorted:
		unsorted = False
		counter += 1
		print(counter)
		if counter == length:
			break
		for k in range(len(arr)):
			print(k)
			try:
				
				if arr[k] >= arr[k+1]:
					
					sorted[k] = arr[k]
					sorted[k+1] = arr[k+1]
					arr[k] = sorted[k+1]
					arr[k+1] = sorted[k]
					print(arr)
			except:
				print('error')
				unsorted = True
	return arr
	


list = [4,3,2,1, 7,9,8,12,60]
s = list[:]
bubble(list)


