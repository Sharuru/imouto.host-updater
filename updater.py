#-*-coding:utf-8 -*-
__author__ = 'Mave'

import re
import urllib2
import platform
import os

reload(__import__('sys')).setdefaultencoding('utf-8')


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


def get_hosts_dl_link(source):
    rule = '<a href="/sources/{id}/(.*)/hosts.*</a>'.format(id=source)
    hosts = re.compile(rule)
    return hosts.findall(content)[0]


def check_local_version(hosts_data):
    version = re.compile('UPDATE_TIME (.*)')
    try:
        return version.findall(hosts_data)[0]
    except IndexError:
        return 'Not Found.'


def check_remote_version(source):
        rule = '<img src="/sources/{id}/icon.jpg".*?>.*?</th>.*?<th>.*?</th>.*?<th>(.*?)</th>'.format(id=source)
        version = re.compile(rule, re.S)
        return version.findall(content)[0]

urls = 'https://www.projecth.us/sources/'

content = linker(urls).decode('utf-8')

############### CONFIG HERE ###############

source_id = 9       # imouto.hosts' id is 9

############### GLOBAL FLAG ###############

hosts_created_by_updater = False
custom_hosts_backed_up = False

###########################################

print 'Checking remote...'

remote_update_date = check_remote_version(source_id)
print 'Latest update time is: ' + remote_update_date

# Local Check
print 'Checking local...'
try:        # Is Local Hosts File Exist Or Not
    local_hosts_data = open('hosts', 'r').read()        # Exist, transport data
except IOError:
    print 'No local hosts found.'       # Not exist, create empty file and transport
    local_hosts_data = open('hosts', 'w+').read()
    hosts_created_by_updater = True

local_update_date = check_local_version(local_hosts_data)

print 'Local hosts file update time is: ' + local_update_date

if local_update_date == 'Not Found.':
    if hosts_created_by_updater is False:
        print 'Maybe this is your first time using hosts on projecth.org/sources.'
        print 'I will backup it :)'
        # Backup Custom Hosts Record
        print 'Backing-up local custom hosts record...',
        custom_hosts = []
        for lines in local_hosts_data:
            custom_hosts.append(lines)
        print 'Success.'
        custom_hosts_backed_up = True
    else:
        print 'No custom hosts record needs backup.'

# Is Hosts Need Update Or Not
if cmp(local_update_date, remote_update_date) == 0:
    print 'Hosts is already updated.'
else:
    print 'Hosts needs update.'

    # Prepare To Download
    download_url = urls + str(source_id) + '/' + get_hosts_dl_link(source_id) + '/hosts'
    print 'Downloading latest imouto.hosts from ' + download_url,

    # Get Remote Data
    remote_hosts_data = urllib2.urlopen(download_url).read()
    open('remote', 'wb').write(remote_hosts_data)
    remote_hosts_data = open('remote', 'r').readlines()

    print 'Success.'

    print 'Ready to modify local hosts...',

    if custom_hosts_backed_up is False:
        # Locate Local Hosts
        local_hosts_data = open('hosts', 'r').readlines()
        total_lines = 0
        update_hosts_lines = 0
        count_hosts = True
        for lines in local_hosts_data:
            total_lines += 1
            if count_hosts is True:
                update_hosts_lines += 1
            if lines == '#+END\n':
                print 'Locate mark found.'
                count_hosts = False

        # Backup Custom Hosts Record
        print 'Backing-up local custom hosts record...',
        custom_hosts = []
        for lines in range(update_hosts_lines, total_lines):
            custom_hosts.append(local_hosts_data[lines])
        print 'Success.'
    else:
        print 'Skipped.'

    # Update Hosts
    print 'Writing remote hosts record...',
    open('hosts', 'w').writelines(remote_hosts_data)
    print 'Success.'
    open('hosts', 'a').write('\n')
    print 'Writing local custom hosts record...',
    open('hosts', 'a').writelines(custom_hosts)
    print 'Success.'
    open('hosts').close()

    print 'Removing temporary file...',
    os.remove('remote')
    print 'Success.'

    print 'Detecting OS type...'
    system_type = platform.system()
    if system_type == 'Windows':
        print 'For Windows, running ipconfig/flushdns...'
        os.system('ipconfig /flushdns')

    print 'All operation finished.'








