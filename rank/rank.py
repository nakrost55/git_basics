#!usr/bin/env python3
# i dont know how to sort , when names are equal
def main (argv):
	
    script, *args = argv
   
    final=rank (args)
    for i in final:
    	print(i[0], i[1])
    
def rank (beetle):
	my_reverse= True
	
	if beetle[0] == '--inv': 
		beetle=beetle[1:]
		my_reverse = False

	for i in range (len(beetle)):
		beetle[i]= beetle[i].split(":")
		beetle[i][0]=beetle[i][0].capitalize() 
		beetle[i][1]=int (beetle[i][1])
	
		
	beetle.sort(key=lambda x: x[1])	
	if my_reverse is True:
		return beetle[::-1]
	else: 
		return beetle
	
		
		   
	
		
			
			
		
		
		



if __name__ == '__main__':
    import sys
    main(sys.argv)
