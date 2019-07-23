# copy-to-flash.py
#
# copy running-config to user defined media (flash:,bootflash:,bootdisk:)
# creates file in device media named hostname-YYYYmmdd-HHMMSS.ios
#

# import modules
from __future__ import print_function, unicode_literals
from netmiko import ConnectHandler
import getpass
from datetime import datetime

# prompt for hostname,user,pw
host = input('host:')
user1 = input('Username:')
p = getpass.getpass()

# create device object
device = {
    'host': host,
    'username': user1,
    'password': p,
    'device_type': 'cisco_ios',
}

# create start time for script running time
start_time = datetime.now()

# convert datetime to a string for use in filename
datetimeStr = start_time.strftime("%Y%m%d-%H%M%S")

print("\n")
print("Establishing SSH session...")

# establish ssh connection to device
net_connect = ConnectHandler(**device)

print("...Connected!")
print("\n")

# user input for media type (flash,bootflash,bootdisk,etc)
media = input('Enter media (flash,bootflash,bootdisk,etc): ')

# define command to send to device along with filename based on host and timestamp
command = 'copy run ' + media + ':' + host + '-' + datetimeStr + '.ios'

# execute command and handle filename prompt
output = net_connect.send_command(command, expect_string=r'Destination filename')

# end time for script running time
end_time = datetime.now()

# disconnects ssh session 
net_connect.disconnect()

# output success msg and script run time
print("\n")
print("#" * 60) 
print("   Successfully created file " + host + '-' + datetimeStr)
print("#" * 60) 
print("\n")
print("SSH session ended.")
print("Total script time: {}".format(end_time - start_time))