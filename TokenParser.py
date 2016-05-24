#!/usr/bin/env python
# encoding: utf-8

import os
import MySQLdb
import commands
import sys
from MysqlDb import MysqlClient
from config import loadGlobalConf


class TokenParser(object):
    def __init__(self, mysqlClient):
        self.mysqlClient = mysqlClient

    def parserLines(self, local_file_dir):
        for filename in os.listdir(local_file_dir):
            print filename
            filename = os.path.join(local_file_dir, filename)
            print filename
            file_object = open(filename, "r")
            cnt = 0
            records = []
            for linetext in file_object.readlines():
                linetext = linetext.strip('\n')
                str_split = linetext.split('|')
                if str_split[0] != '':
                    cnt = cnt + 1
                    recordTime = str_split[0]
                    token = str_split[20].partition("token=")
                    serviceStarttime1 = str_split[20].partition("start-time=")
                    serviceStarttime2 = serviceStarttime1[2].split('&')[0]
                    serviceStarttime3 = serviceStarttime2.replace('T','')
                    serviceStarttime = serviceStarttime3.replace('Z','')
                    serviceStoptime1 = str_split[20].partition("stop-time=")
                    serviceStoptime2 = serviceStoptime1[2].split('&')[0]
                    serviceStoptime3 = serviceStoptime2.replace('T','')
                    serviceStoptime = serviceStoptime3.replace('Z','')
                    serviceDuration = str_split[28]
                    token_split = token[2].split('&')
                    token = token_split[0]
                    rs = decodeToken("java", "-jar", "decodeToken.jar", "i\ am\ aoteman", token)
                    if (token != '' and  len(rs.split(':'))>= 2 ):
                        getTokenUser = rs.split(':')
                        userAndContent_split = getTokenUser[1].split('|')
                        userId = userAndContent_split[0]
                        channelName = userAndContent_split[5]
                        channelContentId = userAndContent_split[3]
                        channelContentAssetId = userAndContent_split[14]
                        channelContentFormat = userAndContent_split[4]
                        channelContentBitrate = userAndContent_split[15]
                        channelContentBitrate = channelContentBitrate.split('\n')[0]
                        # print("recordTime:", recordTime)
                        # print("serviceStarttime:", serviceStarttime)
                        # print("serviceStoptime:", serviceStoptime)
                        # print("serviceDuration:", serviceDuration)
                        # print("getTokenUser[1]",getTokenUser[1])
                        # print("userId",userId)
                        # print("channelName",channelName)
                        # print("channelContentId",channelContentId)
                        # print("channelContentAssetId",channelContentAssetId)
                        # print("channelContentFormat",channelContentFormat)
                        # print("channelContentBitrate",channelContentBitrate)
                        if cnt == 1000:
                            #write to db
                            self.mysqlClient.batchInsert("VSTORAGE" , records)
                            print 'write to db success ' + str(cnt)
                            cnt = 0
                            records = []
                        cnt = cnt + 1
                        records.append(
                            [recordTime, serviceStarttime, serviceStoptime, serviceDuration, userId, channelName,
                             channelContentId, channelContentAssetId, channelContentFormat, channelContentBitrate])
                    else:
                        print 'token有问题: %s' %(token)
                else:
                    continue
            if len(records) > 0:
                self.mysqlClient.batchInsert("VSTORAGE" , records)
            file_object.close()


def decodeToken(*args):
    stat, text = commands.getstatusoutput((' ').join(args))
    if stat != 0:
        raise Exception("decode token error")
    return text
