__author__ = 'lee'

from file_download import *
from MysqlDb import MysqlClient
from config import loadGlobalConf
import  sys , os
from TokenParser import  *


def get_curr_dir():
    import datetime
    lastDate = datetime.date.today() - datetime.timedelta(days=1)
    dateDir = lastDate.strftime('%Y%m%d')
    return "/"+dateDir

if __name__ == '__main__':
    """ main entry
     1.parse config ,
     2.download ftp files ,
     3.save to db
    """

    reload(sys)
    sys.setdefaultencoding('utf-8')

    globalConfig = loadGlobalConf()
    print globalConfig

    datetimes = ['20151126','20151128','20151129']
    for datetime in datetimes:
        remote_dir = "/" + datetime
        local_dir =  "/data/timeshiftdata/" + datetime
        #remote_dir = get_curr_dir()
        #remote_dir = '/20151123'
        #local_dir =  globalConfig['local_dir'] + remote_dir
        #local_dir = '/data/timeshiftdata/20151123'
        #os.makedirs(local_dir)
        print "fetch dir " + remote_dir
        # init downloader
        ftp = FtpDownload(globalConfig['ftpIp'])
        #init mysqlclient
        mysqlClient = MysqlClient(globalConfig['mysqlIp'],globalConfig['mysqlUserName'], globalConfig['mysqlPwd'], '3306', 'python')
        mysqlClient.connect()
        db = globalConfig['mysqlDb']
        #init token parser
        tokenParser = TokenParser(mysqlClient)

        #start to work
        ftp.connect(globalConfig['ftpUserName'], globalConfig['ftpPwd'])
        #ftp.download(remote_dir,local_dir, ".log")

        tokenParser.parserLines(local_dir)
