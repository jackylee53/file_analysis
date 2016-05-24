__author__ = 'lee'
import json
import os
import logging.config

def loadGlobalConf():
    globalConfFileName = "config/config.json"

    if not os.path.exists(globalConfFileName):
        globalConfFileName = "config/config.json.tmp"

    with open(globalConfFileName) as conf_file:
        globalConf = json.load(conf_file)

    return globalConf

if __name__ == '__main__':
    print  loadGlobalConf()