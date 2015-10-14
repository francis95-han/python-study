# coding = utf-8webpage

__author__ = 'bohan'

filename = raw_input('Enter filename:')
try:
    f = open(filename, 'r')
    for eachline in f:
        print eachline
    f.close()
except IOError:
    print 'couldn\'t open '+filename

