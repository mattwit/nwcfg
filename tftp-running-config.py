#
# capture running-config through tftp
# script prompts for tftp server IP
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
device1 = {
    'host': host,
    'username': user1,
    'password': p,
    'device_type': 'cisco_ios',
}

# create start time for script running time
start_time = datetime.now()

# establish ssh connection to device
net_connect = ConnectHandler(**device1)

# prompt for tftp server host or IP
tftp = input('tftp server IP:')

# define command to send file from device to unser specified tftp server 
command = 'copy run tftp://' + tftp

# execute command and handle filename prompt
output = net_connect.send_command(command, expect_string=r'destination filename')

# changes running-config name to the host names with an extension of .ios
output += net_connect.send_command(
        host +'.ios', 
        expect_string=r'vrf',
    )

# end time for script running time
end_time = datetime.now()

# disconnects ssh session 
net_connect.disconnect()

# output success msg and script run time
print("\n")
print("#" * 60) 
print("Success!")
print("Total time: {}".format(end_time - start_time))
print("#" * 60) 
print("\n")