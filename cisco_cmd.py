# cisco.cmd.py 
#
# user imput of a command in global config mode
# output of command writes to console
# 

# import modules
from netmiko import ConnectHandler
import getpass
import subprocess
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

print("\n")
print("Establishing SSH session...")

#establish ssh connection to device
net_connect = ConnectHandler(**device1)

print("...Connected!")
print("\n")

# define command to send to device
command = input('enter command:')

# send command to device and disconnect
output = net_connect.send_command(command)

# disconnects ssh session 
net_connect.disconnect()

# end time for script running time
end_time = datetime.now()

#print output to console
print("\n")
print("#" * 80) 
print(output)
print("#" * 80) 
print("\n")
print("SSH session ended.")
print("Total time: {}".format(end_time - start_time))
print("\n")   