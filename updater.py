#-*-coding:utf-8 -*-
__author__ = 'Mave'

import re
import urllib.request
import platform
import os


def linker(url):
    linker_try_times = 3
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Macho Macho Man')
    for times in range(linker_try_times):
        print('Connecting...', end='')
        try:
            response = urllib.request.urlopen(req, timeout=5)
            print('Success.')
            return response.read()
        except:
            print('Failed, Try Again.')
            pass
        if times == 2:
            print('Connection Failed.')
            print('Please check your hosts or try again later.')
            exit()


def backup_local_hosts(data):
    hosts_data_local = []
    print('Detecting local hosts type...', end='')
    for check_line in data:
        if check_line == '#+END\n':
            print('Formatted.')
            # Locate Local Hosts
            total_lines = 0
            update_hosts_lines = 0
            count_hosts = True
            for lines in data:
                total_lines += 1
                if count_hosts is True:
                    update_hosts_lines += 1
                if lines == '#+END\n':
                    print('Locate mark found.')
                    count_hosts = False
            # Backup Process
            print('Backing-up local custom hosts record...', end='')
            for record in range(update_hosts_lines, total_lines):
                hosts_data_local.append(data[record])
            print('Success.')
            return hosts_data_local
    print('Not formatted.')
    print('Backing-up local custom hosts record...', end='')
    for record in data:
        hosts_data_local.append(record)
    print('Success.')
    return hosts_data_local


def check_local_hosts():
    print('Checking local...')
    try:
        hosts_data_check = open('hosts', 'r', encoding='utf-8').readlines()
    except IOError:
        print('No local hosts found.')
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


def check_remote_version(hosts_data):
    rule = 'UPDATE_TIME (.*)'
    version = re.compile(rule)
    return version.findall(hosts_data)[0]


# Main Start
urls = 'https://raw.githubusercontent.com/zxdrive/imouto.host/master/imouto.host.txt'
remote_hosts_data = linker(urls)
content = remote_hosts_data.decode('utf-8')
print('Checking remote...')
remote_update_date = check_remote_version(content)
print('Latest update time is: ' + remote_update_date)

# Local Check
local_hosts_data = check_local_hosts()
local_update_date = check_local_version(local_hosts_data)
print('Local hosts file update time is: ' + local_update_date)

# Is Hosts Need Update Or Not
remote_update_date = remote_update_date.strip('\r')
if local_update_date == remote_update_date:
    print('Hosts is already updated.')
else:
    print('Hosts needs update.')

    # Ready to Update Hosts
    print('Ready to update local hosts...')

    # Backup Custom Hosts Record
    custom_hosts = backup_local_hosts(local_hosts_data)

    # Update Hosts
    print('Writing remote hosts record...', end='')
    open('hosts', 'wb').write(remote_hosts_data)
    print('Success.')
    open('hosts', 'a').write('\n')
    print('Writing local custom hosts record...', end='')
    open('hosts', 'a').writelines(custom_hosts)
    print('Success.')
    open('hosts').close()

    # Flush Dns
    print('Detecting OS type...')
    system_type = platform.system()
    if system_type == 'Windows':
        print('For Windows, running ipconfig/flushdns...')
        os.system('ipconfig /flushdns')

# All Finished
print('All operation finished.')
