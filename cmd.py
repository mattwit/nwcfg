# output user defined global conf command to console
# write output to file
# txt file saved to same directory as script

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

# convert datetime to a string for use in filename
datetimeStr = start_time.strftime("%Y%m%d-%H%M%S")

# establish ssh connection to device
net_connect = ConnectHandler(**device1)

# define text file
file = open(host + '-' + datetimeStr + '_cmd.txt', 'w')

# prompt user for command to define command to send to device
command = input('enter global config command:')

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
	
# Write output to file and close
file.write(output)
file.close()