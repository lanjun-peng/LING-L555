#read the file line by line
import sys
m = {}
freq = {}
for line in sys.stdin.readlines():
	line = line.strip('\n')
	if '\t' not in line:
		continue
	row = line.split('\t')
	if len(row) != 10:
		continue
	token = row[1]
	tag = row[3]
	if tag not in freq:
		freq[tag] = 0
	freq[tag]+=1
#create matrix for the word to tag
	if token not in m:
		m[token] = {}
	if tag not in m[token]:
		m[token][tag]=0
	m[token][tag] = m[token][tag]+1


for token in m:
	for tag in m[token]:
		print(m[token][tag]/sum(m[token].values()),m[token][tag],token,tag)


#make frequency percentage for tags
for (k,v) in freq.items():
	print(v/sum(freq.values()),k)

"""
#creat the final output
x = ['# P','count','tag','form']
Y = ['freq','vocab[tag]','tag','token']
print('\t' + '\t'.join(x))
for yy in y:
        print(yy, end='\t')
	for xx in x:
        	print('_',end='\t')
	print()
"""
