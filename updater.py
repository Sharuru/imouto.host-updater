#-*-coding:utf-8 -*-
__author__ = 'Mave'

import re
import urllib2
import platform

reload(__import__('sys')).setdefaultencoding('utf-8')

system_type = platform.system()


def linker(url):
    linker_try_times = 3
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Macho Macho Man')
    for times in range(linker_try_times):
        print 'Connecting...',
        try:
            response = urllib2.urlopen(url, timeout=5)
            print 'Success.'
            return response.read()
        except:
            print 'Failed, Try Again.'
            pass
        if times == 2:
            print 'Connection Failed.'
            print 'Please check your hosts or try again later.'
            exit()


def get_hosts(source):
    if source == 9:      # imouto.hosts' id is 9
        hosts = re.compile('<a href="/sources/9/(.*)/hosts.*</a>')
        return hosts.findall(content)[0]


def check_hosts_version(hosts_data):
    version = re.compile('UPDATE_TIME (.*)')
    try:
        return str(version.findall(hosts_data)[0])
    except IndexError:
        return 'Not Found.'


def check_remote_version(source):
    if source == 9:     # imouto.hosts' id is 9
        version = re.compile('<img src="/sources/9/icon.jpg".*?>.*?</th>.*?<th>.*?</th>.*?<th>(.*?)</th>', re.S)
        return version.findall(content)[0]


urls = 'https://www.projecth.us/sources/'

content = linker(urls).decode('utf-8')

source_id = 9       # imouto.hosts' id is 9
print 'Finding imouto.hosts...'

local_hosts = open('localhosts', 'r')
local_hosts_data = local_hosts.read()
remote_update_date = check_remote_version(9)
local_update_date = check_hosts_version(local_hosts_data)

print 'Latest update time is: ' + remote_update_date

print 'Local hosts file update time is: ' + local_update_date
if local_update_date == 'Not Found.':
    print 'May this is your first time using imouto.hosts'

if cmp(local_update_date, remote_update_date) == 0:
    print 'Hosts is already updated.'
else:
    print 'Hosts needs update.'

    download_url = urls + str(source_id) + '/' + get_hosts(source_id) + '/hosts'
    print 'Downloading latest imouto.hosts from ' + download_url,

    remote_hosts = urllib2.urlopen(download_url)
    remote_hosts_data = remote_hosts.read()
    
    print 'Success.'







