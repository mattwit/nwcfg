

from datetime import datetime
import getpass 

uname = getpass.getuser()
passwd = getpass.getpass(prompt='password: ', stream=None)

devices = {

    'server1' : {
        'device_type':'cisco_ios',
        'host':'10.10.10.1',
        'username':uname, 
        'password':passwd 
    },

    'server2' : {
        'device_type':'cisco_ios',
        'host':'10.10.10.2',
        'username':uname, 
        'password':passwd 
    },

    'server3' : {
        'device_type':'cisco_ios',
        'host':'10.10.10.3',
        'username':uname, 
        'password':passwd 
    },

    'server4' : {
        'device_type':'cisco_ios',
        'host':'10.10.10.4',
        'username':uname, 
        'password':passwd 
    }
}