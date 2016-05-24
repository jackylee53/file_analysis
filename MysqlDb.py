__author__ = 'lee'
# coding = utf-8
import MySQLdb
import sys

# def writemysqldb(*args):

class MysqlClient(object):
    def __init__(self, host, user, passwd, port, dbName):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.dbName = dbName

    def connect(self):
        self.conn = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, port=int(self.port),
                                    charset='utf8')
        self.conn.select_db(self.dbName)

    def close(self):
        self.conn.close()

    def insert(self, table, record):
        cur = self.conn.cursor()
        formated_sql = 'insert into ' + table + '  values("'
        formated_sql = formated_sql + '", "'.join(record) + '" )'
        print formated_sql
        cur.execute(formated_sql)
        self.conn.commit()
        cur.close()


    def batchInsert(self, table, records):
        cur = self.conn.cursor()
        formated_sql = 'insert into ' + table + '  values '
        for r in records:
            formated_sql = formated_sql + '("' + '", "'.join(r) + '" ),'
        print formated_sql
        cur.execute(formated_sql[0:-1])
        self.conn.commit()
        cur.close()


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    mysqlClient = MysqlClient('30.209.81.7', 'root', 'root', '3306', 'python')
    mysqlClient.connect()
    # mysqlClient.insert('VSTORAGE',
    #                    ['20151124151640', '20151124151445', '20151124151640', '115', '1104003091900024C133DB82',
    #                     '1104003091900024C133DB82', 'icms0000000000000000000004365177', '30CP230120140408871400',
    #                     'video/h264', '2500000'])
    mysqlClient.batchInsert('VSTORAGE',
                            [['20151124151640', '20151124151445', '20151124151640', '115', '1104003091900024C133DB82',
                              '1104003091900024C133DB82', 'icms0000000000000000000004365177', '30CP230120140408871400',
                              'video/h264', '2500000'],
                             ['20151124151640', '20151124151445', '20151124151640', '115', '1104003091900024C133DB82',
                              '1104003091900024C133DB82', 'icms0000000000000000000004365177', '30CP230120140408871400',
                              'video/h264', '2500000']])
    mysqlClient.close()
