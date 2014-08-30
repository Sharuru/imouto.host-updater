#-*-coding:utf-8 -*-
__author__ = 'Mave'

import re
import urllib2
import platform
import os

reload(__import__('sys')).setdefaultencoding('utf-8')


############### CONFIG HERE ###############

source_id = 9       # imouto.host's id is 9

###########################################


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


def backup_local_hosts(data):
    hosts_data_local = []
    print 'Detecting local hosts type...',
    for check_line in data:
        if check_line == '#+END\n':
            print 'Formatted.'
            # Locate Local Hosts
            total_lines = 0
            update_hosts_lines = 0
            count_hosts = True
            for lines in data:
                total_lines += 1
                if count_hosts is True:
                    update_hosts_lines += 1
                if lines == '#+END\n':
                    print 'Locate mark found.'
                    count_hosts = False
            # Backup Process
            print 'Backing-up local custom hosts record...',
            for record in range(update_hosts_lines, total_lines):
                hosts_data_local.append(data[record])
            print 'Success.'
            return hosts_data_local
    print 'Not formatted.'
    print 'Backing-up local custom hosts record...',
    for record in data:
        hosts_data_local.append(record)
    print 'Success.'
    return hosts_data_local


def get_hosts_dl_link(source):
    rule = '<a href="/sources/{id}/(.*)/hosts.*</a>'.format(id=source)
    hosts = re.compile(rule)
    return hosts.findall(content)[0]


def check_local_hosts():
    print 'Checking local...'
    try:
        hosts_data_check = open('hosts', 'r').readlines()
    except IOError:
        print 'No local hosts found.'
        hosts_data_check = open('hosts', 'w+').readlines()
    return hosts_data_check


def check_local_version(hosts_data):
    rule = 'UPDATE_TIME (.*)'
    version = re.compile(rule)
    for line_for_check in hosts_data:
        try:
            return version.findall(line_for_check)[0]
        except IndexError:
            pass
    return 'Not Found.'


def check_remote_version(source):
        rule = '<img src="/sources/{id}/icon.jpg".*?>.*?</th>.*?<th>.*?</th>.*?<th>(.*?)</th>'.format(id=source)
        version = re.compile(rule, re.S)
        return version.findall(content)[0]


# Main Start
urls = 'https://www.projecth.us/sources/'
content = linker(urls).decode('utf-8')
print 'Checking remote...'
remote_update_date = check_remote_version(source_id)
print 'Latest update time is: ' + remote_update_date

# Local Check
local_hosts_data = check_local_hosts()
local_update_date = check_local_version(local_hosts_data)
print 'Local hosts file update time is: ' + local_update_date

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
    print 'Ready to update local hosts...'

    # Backup Custom Hosts Record
    custom_hosts = backup_local_hosts(local_hosts_data)

    # Update Hosts
    print 'Writing remote hosts record...',
    open('hosts', 'w').writelines(remote_hosts_data)
    print 'Success.'
    open('hosts', 'a').write('\n')
    print 'Writing local custom hosts record...',
    open('hosts', 'a').writelines(custom_hosts)
    print 'Success.'
    open('hosts').close()

    # Remove Remote
    print 'Removing temporary file...',
    os.remove('remote')
    print 'Success.'

    # Flush Dns
    print 'Detecting OS type...'
    system_type = platform.system()
    if system_type == 'Windows':
        print 'For Windows, running ipconfig/flushdns...'
        os.system('ipconfig /flushdns')

# All Finished
print 'All operation finished.'








