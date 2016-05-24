"""
 Description: test_ftp
 Author: xbkaishui
 Update: xbkaishui(2015-11-28 10:24)

"""
# !/usr/bin/env python

from ftplib import FTP
from time import sleep
import os


class FtpDownload(object):
    def __init__(self, host):
        self.ftp = FTP(host)
        self.my_dirs = []  # global
        self.my_files = []  # global
        self.curdir = ''  # global


    def connect(self, user, pwd):
        if user is not None:
            self.ftp.login(user, pwd)
        else:
            self.ftp.login()

    def close(self):
        self.ftp.quit()


    def download(self, remote_dir, local_dir, suffix):
        self.suffix = suffix
        try:
            if local_dir is None:
                local_dir = "/tmp"
            print ("remote_dir:",remote_dir)
            print ("local_dir:",local_dir)            
            self.check_dir(remote_dir)  # directory to start in
            self.ftp.cwd('/.')# change to root directory for downloading
            for f in self.my_files:
                print('getting ' + f)
                # file_name = f.replace('/', '_')  # use path as filename prefix, with underscores
                file_name = os.path.basename(f)
                print file_name
                full_file_path = os.path.join(local_dir, file_name)
                print 'save to %s ' %(full_file_path)
                self.ftp.retrbinary('RETR ' + f, open(full_file_path, 'wb').write)
                sleep(1)
        except Exception, e:
            print('oh dear. %s ', e)
            self.ftp.quit()
        print('all done!')


    def get_dirs(self, ln):
        cols = ln.split(' ')
        objname = cols[len(cols) - 1]  # file or directory name
        if ln.startswith('d'):
            self.my_dirs.append(objname)
        else:
            if objname.endswith(self.suffix):
                self.my_files.append(os.path.join(self.curdir, objname))  # full path


    def check_dir(self, adir, ):
        # global my_dirs
        # global my_files  # let it accrue, then fetch them all later
        # global curdir
        self.my_dirs = []
        gotdirs = []  # local
        curdir = self.ftp.pwd()
        print("going to change to directory " + adir + " from " + curdir)
        self.ftp.cwd(adir)
        self.curdir = self.ftp.pwd()
        print("now in directory: " + curdir)
        self.ftp.retrlines('LIST', self.get_dirs)
        gotdirs = self.my_dirs
        print("found in " + adir + " directories:")
        print(gotdirs)
        print("Total files found so far: " + str(len(self.my_files)) + ".")
        sleep(1)
        for subdir in gotdirs:
            self.my_dirs = []
            self.check_dir(subdir)  # recurse
        self.ftp.cwd('..')  # back up a directory when done here


if __name__ == '__main__':
    host = ftpIp
    remote_dir = ftpRemotedir
    local_dir = ftpDownloadLocaldir
    ftp = FtpDownload(host)
    ftp.connect(ftpUserName,ftpPwd)
    ftp.download(remote_dir, local_dir, ".log")



