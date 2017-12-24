# word parser v 0.1.1 
from sys import argv
import re
filename = argv[1]
counts = dict()

def process (line):
#    print (line.lower())
    words = re.split('\.|\!|\?|\,|\;|\=|\#|\:|\+|\-|\_|\@|\*|\<|\$|\~|\[|\]|\(|\)|\/|%|\"|\'|\s',line.lower())
#    print words
    for i in words:
      counts[i] = counts.get(i, 0) + 1
    return

with open(filename) as f:
    for line in f:
        process(line)

counts.pop("", None)
for key in sorted(counts.iterkeys()):
    print "%s: %s" % (key, counts[key])

