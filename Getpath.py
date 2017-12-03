#!/usr/bin/env python
# -*- coding:utf8 -*-

import os
import shutil
import hashlib

def md5sum(filename):
    fd = open(filename,"r")
    fcont = fd.read()
    fd.close()
    fmd5 = hashlib.md5(fcont)
    return fmd5


def  getpath(filename):
    dir='/home/dxhy'
    realpath=''
    backdir='/home/dxhy/backup'
    for paredir,childdir,files in os.walk(dir):
         for name in files:
            if name == filename:
                fullpath="%s/%s"%(paredir,name)
                res = fullpath.split('/')
                for i in res:
                    if i not in ['logs','update','backup'] and  i == 'webapps':
                        realpath = fullpath
    if realpath:
        #print realpath '打印日志'
        shutil.copy(realpath,backdir)
        shutil.copy(filename,realpath)
        a=md5sum(filename).hexdigest()
        b=md5sum(realpath).hexdigest()
        if a == b:
            print 'ok'
        else:
            print "failed"
    else:
        print 'no exists'

if __name__ == '__main__':
    upfiles=['a.txt','b.txt']
    for filename in upfiles:
        getpath(filename)