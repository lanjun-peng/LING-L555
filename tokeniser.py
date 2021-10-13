import sys

counter = 0

# Read in one line at a time 
line = sys.stdin.readline()
while line:

#replace space with a newline
#	line=line.replace(' ','\n')

#add space before or after punctuation characters
	line=line.replace(',',' , ')
	line=line.replace(':',' : ')
	line=line.replace('(',' ( ')
	line=line.replace(')',' ) ')
	
#count 
	counter=counter+1
	print(counter)
#print output
#loop for splitting the lines
	tokens=line.split()

#count tokens
	tcounter=0
	for token in tokens:
		tcounter=tcounter+1
		print(tcounter,token)
	line = sys.stdin.readline()
