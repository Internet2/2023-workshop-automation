# pip install --user textfsm
# pip install --user netmiko
import json
from netmiko import Netmiko
from pprint import pprint

username = "fill me in!"
password = "fill me in!"
device_type = "fill me in!"
hosts = ["x.x.x.x", "y.y.y.y"]
command_to_run = "show int brief"

for host in hosts:
  # Create a variable that represents an SSH connection to our router.
  connection = Netmiko(
    username=username,
    password=password,
    device_type=device_type,
    ip=host,
  )

  # Send a command to the router, and get back the output "dictionaried" by textfsm.
  textfsm_output = connection.send_command(command_to_run, use_textfsm=True)
  
  print(f"### This is the TextFSM output from {host}: ###")
  print(textfsm_output)
  print("\n") # Add extra space between our outputs for each host


  print(f"### This is the TextFSM output from {host}, but JSON-formatted: ###")
  print(json.dumps(textfsm_output, indent=4)) # indent for readability
  print("\n") # Add extra space between our outputs for each host
