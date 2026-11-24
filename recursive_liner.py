
def liner(counter):
	"""recursively drawing english liner."""
	if counter != 0:
		print('-'*5)
		for i in range(1,4):
			print('-')
		counter -= 1
		liner(counter)
	else:
		print('-'*5)

	
	



