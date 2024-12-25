import numpy as np

def calculate(list) :
	array = np.array(list)
	if len(list)  !=9 :
		
		raise ValueError ('List must contain nine numbers.')
	array  = array.reshape((3,3))
	
		
	mean = [array.mean(axis = i).tolist() for i in (0,1, None)]
	var = [array.var(axis = i).tolist() for i in (0,1,None)]
	std = [array.std(axis = i).tolist() for i in (0,1,None)]
	max = [array.max(axis = i).tolist() for i in (0,1,None)]
	min = [array.min(axis = i).tolist() for i in (0,1,None)]
	sum = [array.sum(axis = i).tolist() for i in (0,1,None)]
	calculations = {'mean' : mean, 'variance' : var , 'standard deviation' : std , 'max' : max , 'min' : min , 'sum' : sum }
	return calculations
