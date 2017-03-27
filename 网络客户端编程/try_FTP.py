# coding:utf-8
#可添加功能如GUI等制作成一个FTP连接工具
__author__ = 'love_huan'

import ftplib, os, socket

HOST = input('你要连接的FTP站点')
DIRN = input('你所需下载的文件的路径')
FILE = input('你要下载的文件名')


def main():
    try:
        f = ftplib.FTP(HOST)

    except (socket.error, socket.gaierror), e:
        print('ERROR:can\'t reach "%s" ' % HOST)
        return
    print('***Connected to host "%s"' % HOST)

    try:
        f.login()
    except ftplib.error_perm:
        print("ERROR:can\'t login anonymously")
        f.quit()
        return
    print('***Logged in as "anonymous"')

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print('ERROR:can\'t CD to "%s" ' % DIRN)
        f.quit()
        return
    print('***Changed to "%s" folder' % DIRN)

    try:
        f.retrbinary('RETR %s' % FILE,open(FILE,'wb').write)
    except ftplib.error_perm:
        print('ERROR:cannot read file "%s"' % FILE)
        os.unlink(FILE)
    else:
        print('***Downloaed "%s" to CWD' % FILE)
        f.quit()
        return

if __name__ == '__main__':
    main()
