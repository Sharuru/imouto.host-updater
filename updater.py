#-*-coding:utf-8 -*-
__author__ = 'Mave'

import requests

reload(__import__('sys')).setdefaultencoding('utf-8')


def linker(url):
    linker_try_times = 3
    headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'  # This is another valid field
    }
    response = requests.get(url, headers=headers)
    print response.status_code
    print response.text
    for times in range(linker_try_times):
        print 'Connecting...',
        try:
            print 'tried'
            response = urllib2.urlopen(request, timeout=5)
            print response.read()
            #return response.read()
        except:
            print 'Failed, Try Again.'
            pass

urls = 'https://www.projecth.us/sources'
#urls = 'https://www.alipay.com'
linker(urls)
