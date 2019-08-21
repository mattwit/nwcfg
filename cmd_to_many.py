# issue a command to multiple devices
# devices are listed in a text file named "hosts.txt"
# output written to text file named "output.txt"

from __future__ import print_function, unicode_literals
from netmiko import ConnectHandler
from datetime import datetime
import getpass
import sys

file_time = datetime.now()
datetimeStr = file_time.strftime("%Y%m%d-%H%M%S")

# class to print output to console and capture to file
class Logger(object):

    def __init__(self):
        self.terminal = sys.stdout
        self.log = open(datetimeStr + "_output.txt", "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        pass 

# login function to read hostfile and input prompt for user credentials
def login():

    # open host file and read to string
    with open("hosts.txt", "r") as f:
        ipaddr = f.read().splitlines()
    f.close()

    #uname = getpass.getuser() #get sername from Windows credentials
    uname = input('username:') #uncomment to prompt for user input
    passwd = getpass.getpass(prompt='Password: ', stream=None)

    return ipaddr,uname,passwd

# function to prompt for user command input and issue command
def cmd():

    hostfile,uname,passwd = login()
    
    command = input("Enter Global Config Command:")

    # call Logger class to print output to console and file
    sys.stdout = Logger()

    # iterate through hostfile for ssh and sending command
    for ipaddr in hostfile:
        device = {
            "device_type": "cisco_ios",
            "ip": ipaddr.strip(),
            "username": uname.strip(),
            "password": passwd.strip(),
        }

        try:
            net_connect = ConnectHandler(**device)

        except Exception:
            print("** Failed to connect.", end="", flush=True)
            continue

        output = net_connect.send_command(command)
        
        print("\n")
        print("#" * 80)
        print(ipaddr)
        print("\n")
        print(output)
        print("#" * 80) 
        print("\n")

    
# main prints script run time
def main():

    start_time = datetime.now()
    
    cmd()

    end_time = datetime.now()

    print("Script Run Time: {}".format(end_time - start_time))
    print("\n")

main()