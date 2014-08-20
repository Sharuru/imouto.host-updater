#-*-coding:utf-8 -*-
__author__ = 'Mave'

import re
import urllib2

reload(__import__('sys')).setdefaultencoding('utf-8')

def linker(url):
    linker_try_times = 3
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Macho Macho Man')
    for times in range(linker_try_times):
        print 'Connecting...',
        try:
            print 'tried'
            response = urllib2.urlopen(url, timeout=5)
            return response.read()
        except:
            print 'Failed, Try Again.'
            pass

urls = 'https://www.projecth.us/sources/'
#urls = 'https://www.alipay.com'
print linker(urls)
