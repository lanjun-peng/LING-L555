#form a dictionary
map = {}
map['che']='ke'
map['cosa']='kosa'
map['chi']='ki'
map['come']='kome'
map['dove']='dove'
map['quale']='kwale'
map['o']='o'
map['d']='d'
map['b']='b'
map['z']='z'
map['f']='f'
map['g']='g'
map['c']='k'
map['l']='l'


#for loop to read by lines
import sys
line = sys.stdin.readline()
while line: 	
	row =line.split('\t')
	if '\t' not in line:
		line=line.strip()
		print(line)
		line=sys.stdin.readline()
		continue
	word=row[1]
	for k in map:
		word = word.replace(k,map[k])
#print the output
#add the word to the existing row
	row[9]='IPA='+word
	print('\t'.join(row))
	line = sys.stdin.readline()
