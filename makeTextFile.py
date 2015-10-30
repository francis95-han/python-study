#coding=utf-8
#!/usr/bin/env python
__author__ = 'bohan'
# 'makeTextFile.py ----create new text file '
import os
ls= os.linesep

#get filename
while True:
    fname = raw_input('please input a file name to save filenames:%s'% ls)
    if os.path.exists(fname):
        print("Error:'%s' already exists" % fname)
    else:
        print('save to ',fname)
        break
#get filr content (text )lines
all = []
print( "\nEnter lines,('.'by itself to quit).\n")

# loop until user terminates input
while True:
    entry =raw_input(">>>")
    if entry == ".":
        break
    else:
        all.append(entry)

# write lines to file with proper line-reading
fobj = open(fname,'w')
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()
print("DONE")



