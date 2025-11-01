import os
from netmiko import ConnectHandler

user = os.getenv("cisco")
password = os.getenv("cisco")

#if not user not password:
 #   raise ValueError("Missing user and password")

device = {
    "device_type" : "cisco_ios"
    "ip" : 192.168.192.185"
    "username": raja,
    "password": cisco,
}

net_connect = ConnectHandler(**device)
output = net_connect.send_command("sh ip int br")
print(output)
