import re

def ip_validate(ip):
    if re.fullmatch(r"192\.168\.\d{1,3}\.\d{1,3}", ip):
        return "Class A"
    elif re.fullmatch(r"172\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip):
        return "Class B"
    elif re.fullmatch(r"10\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip):
        return "Class C"
    else:
        return "Invalid IP"

print("welcome to the networking world")
ip = input("enter the ip address you want to validate: ")
print(ip_validate(ip))
