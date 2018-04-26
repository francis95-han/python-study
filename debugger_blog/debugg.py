# -*- coding: utf-8 -*-
# @Date    : 2016-08-11 16:48:16
# @Author  : giantbranch (giantbranch@gmail.com)
# @Link    : http://blog.csdn.net/u012763794?viewmode=contents

from ctypes import *
from debugger_blog.debugger_defines import *

kernel32 = windll.kernel32


class debugger():

    def __init__(self):
        pass

    def load(self, path_to_exe):
        creation_flags = DEBUG_PROCESS
        startupinfo = STARTUPINFO()
        process_information = PROCESS_INFORMATION()
        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x0
        startupinfo.cb = sizeof(startupinfo)
        if kernel32.CreateProcessA(path_to_exe,
                                   None,
                                   None,
                                   None,
                                   False,
                                   creation_flags,
                                   None,
                                   None,
                                   byref(startupinfo),
                                   byref(process_information)):
            print("[*] we have successfully launched the process!")
            print("[*] PID:%d" % process_information.dwProcessId)
        else:
            print("[*] Error:0x%08x." % kernel32.GetLastError())
