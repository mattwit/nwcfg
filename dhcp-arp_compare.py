# DHCP Address Lease and ARP/MAC Table Compare
# still a work in progress
#
# Merges csv files to help figure out hostnames in switch output of arp or mac table
# Requires DHCP address lease export and switch arp or mac table output (e.g. show arp)
# rename IP Address columns in both csv files to for a common index to sort and merge

# pandas library is required (pandas.pydata.org)
import pandas as pd
from pandas import DataFrame

# read csv file from switch mac table output (arp or mac table)
csv1 = pd.read_csv("MAC.csv")

# read csv file from DHCP server
csv2 = pd.read_csv("DHCP.csv")

# merge csv files keying on common IP address
csv3 = pd.merge(csv1, csv2)

# export output to a csv file named 'merge.csv'
export_csv = csv3.to_csv (r'merge.csv', index = None, header=True)

# print output to console
print(csv3)