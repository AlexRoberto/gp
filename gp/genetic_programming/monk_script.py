'''
Created on 16/03/2014

@author: alex
'''

import sys

if __name__ == '__main__':
    f = open(sys.argv[1],"r")
    w = open(sys.argv[2],"w")
    
    w.write("@attribute Class {0,1}\n")
    w.write("@data\n")
    
    for line in f.readlines():
        line = line.replace("\n", "")
        line = line.replace("\r", "")
        data = line.split()
        del data[0]
        del data[-1]
        w.write(','.join(data)+'\n')
    f.close()
    w.close()