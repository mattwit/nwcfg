# 
# use a text file to send changes to a cisco device
# script will prompt for the change file name
# put your txt change file in the same directory as this script
# change file commands are executed in global config mode
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

# create device 
R1 = {
    'host': host,
    'username': user1,
    'password': p,
    'device_type': 'cisco_ios',
}

# create start time for script running time
start_time = datetime.now()

print("\n")
print("Establishing SSH session...")

#establish ssh connection to device
net_connect = ConnectHandler(**R1)

print("...Connected!")
print("\n")

# user input for name of change file
f = raw_input('Enter change filename:')
change_file = f

# Make configuration changes using an external file
output = net_connect.send_config_from_file(change_file)

# disconnects ssh session 
net_connect.disconnect()

# end time for script running time
end_time = datetime.now()

# print output 
print("\n")
print("#" * 70) 
print(output)
print("#" * 70) 
print("\n")
print("SSH session ended.")
print("\n")

# print script run time
print("Total time: {}".format(end_time - start_time))
print("\n")     