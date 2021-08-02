
#BENFORD'S LAW 
	Using numpy arrays of random floating numbers
	
	Need to figure out how to vary the array size 
	and the way each element gets initialized so
	that it can be adapted across multiple applications
	(when I had the gscale set to a number higher 
	than 9999 the compiler threw an error)
	
	
	Can this be used for error checking in neural networks?
	because it is a percentage and not always an exact "double the amount of 1's" scenario?
	
	Like after each layer it runs the results from each node through a Benford error checker 
	to make sure there isn't anything off? 
