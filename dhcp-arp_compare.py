# DHCP Address Lease and ARP Table Compare
# still a work in progress
#
# Merges csv files to help figure out hostnames in switch output of arp or mac table
# Requires DHCP address lease export and switch arp table output (e.g. show iparp for EXOS)
# Script renames IP Address column for each output and merges indexing on the new common column name

# pandas library is required (pandas.pydata.org)
import pandas as pd
from pandas import DataFrame

# read csv file from switch arp table output (EXOS 'show ip arp' output)
csv1 = pd.read_csv("MAC.csv")

# rename 'Destination' column from EXOS 'show iparp' output
csv1.rename(columns={'Destination':'ipAddress'}, inplace=True)

# read csv file from Windows DHCP server address lease export
csv2 = pd.read_csv("DHCP.csv")

# rename 'Destination' column from Windows DHCP server address lease export
csv2.rename(columns={'Client IP Address':'ipAddress'}, inplace=True)

# merge csv files keying on column 'ipAddress' in both csv files
csv3 = pd.merge(csv1, csv2)

# export output to a csv file named 'merge.csv'
export_csv = csv3.to_csv (r'merge.csv', index = None, header=True)

# print output to console
print(csv3)