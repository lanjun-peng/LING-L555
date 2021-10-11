import sys

# Read in everything from standard input
text = sys.stdin.read()

#replace every full stop '.' followed by a space ' ' with a full stop and a newline
text = text.replace('. ',' .\n')

#output everything to standard output
sys.stdout.write(text)

