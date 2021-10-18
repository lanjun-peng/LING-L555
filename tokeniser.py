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
#print output
#loop for splitting the lines
	tokens=line.split()
	print('# sent_id = %d' % (counter))
	print('# text = %s' % (line.strip())) 

#count tokens
	tcounter=0
	for token in tokens:
		tcounter=tcounter+1
		print('%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_' %(tcounter,token))
	line = sys.stdin.readline()
	print()
