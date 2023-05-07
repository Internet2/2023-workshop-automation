#!/usr/bin/python

import json
import yaml

f = open('output.json')

data = json.load(f)

f.close()

inventory = {'all': {'vars': {'ansible_user': 'clab'}, 'children': {'junos': {'hosts': {}}, 'iosxr': {'hosts':{}}}}}

for host in data:
    if(host['platform'] == 'juniper_junos'):
        inventory['all']['children']['junos']['hosts'][host['name']] = {'device_type': 'JUNOS' }
    elif(host['platform'] == 'cisco_xr'):
        inventory['all']['children']['iosxr']['hosts'][host['name']] = {'device_type': 'IOSXR'}
    else:
        inventory['all']['hosts'][host['name']] = {}

with open('inventory.yaml', 'w') as file:
    yaml.dump(inventory, file)
