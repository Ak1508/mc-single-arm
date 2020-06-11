import pickle, string, os, sys
from itertools import islice

left  =[]
right = []
with open ("c12_2p7_21.035.inp",'r') as f:
    # for line in islice(f, 3, None): # skipping all the headers 
        
     #    print (line)

    line = f.readlines()[3:]
    line = [x.strip(' ') for x in line]
    line = [x.strip('\n') for x in line]
    print (len(line))
    for i, val in enumerate(line):
        print (i, val)
