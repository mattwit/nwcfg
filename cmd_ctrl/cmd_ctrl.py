from netmiko import ConnectHandler
from datetime import datetime
from contextlib import redirect_stdout
from io import StringIO
from sites.des import gear 
from py_mail import py_delivery
import io
import os
import sys

#https://eli.thegreenplace.net/2015/redirecting-all-kinds-of-stdout-in-python/

config = []

def send_cli():
    f = io.StringIO()
    with redirect_stdout(f):
        begin = datetime.now()
        for k, v in gear.devices.items():
            net_connect = ConnectHandler(**v)
            #cmd = net_connect.send_config_set(config)
            cmd = net_connect.send_command("sh ip arp | i Vlan104") 
            print(f"\n\n------Device {k}------")
            print(cmd)
            print("------END------")
        end = datetime.now()
        total_time = end - begin
        print("Executed in", total_time)
    print(f.getvalue())
    global out
    out = f.getvalue()

send_cli()
py_delivery.py_delivery(out)

