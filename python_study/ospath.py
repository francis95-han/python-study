__author__ = 'love_huan'
#coding=utf-8
#!/usr/bin/env python
import os
for tmpdir in ('/tmp',r'c:\temp'):
    if os.path.isdir(tmpdir):
        break
else:
    print 'no temp availabled'
    tmpdir = ''

if tmpdir:
    os.chdir(tmpdir)
    cwd = os.getcwd()
    print '***current temporary directory'
    print cwd
    print '***creating example directory'
    os.mkdir('example')
    os.chdir('example')
    cwd=os.getcwd()
    print '***new working directory'
    print(cwd)
    print '***orginal directory listing'
    print os.listdir(cwd)

    print '***creating test file...'
    fobj= open('test','w')
    fobj.write('foo\n')
    fobj.write('bar\n')
    fobj.close()
    print '*** updated directory listing'
    print os.listdir(cwd)

    print "***renaming 'test' to 'filetest.txt'"
    os.rename('test','filetest.txt')
    print '***updated directory listing'
    print os.listdir(cwd)

    path = os.path.join(cwd,os.listdir(cwd)[0])


