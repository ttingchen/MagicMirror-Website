import bluetooth
import os
import time
import picar_4wd as fc
import sys
import tty
import termios
import asyncio
from picar_4wd.utils import pi_read

power_val = 50

hostMACAddress = "BC:20:CF:80:CD:90" # The address of Raspberry PI Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 0
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)
print("listening on port ", port)


def measure_temp():
    temp = pi_read()
    temperature = temp['cpu_temperature']
    return temperature

def measure_battery()):
    temp = pi_read()
    battery = temp['battery']
    return battery

def car_movement(num):
    if key=='6':
        if power_val <=90:
            power_val += 10
            print("power_val:",power_val)
    elif key=='4':
        if power_val >=10:
            power_val -= 10
            print("power_val:",power_val)
    if key=='w':
        fc.forward(power_val)
    elif key=='a':
        fc.turn_left(power_val)
    elif key=='s':
        fc.backward(power_val)
    elif key=='d':
        fc.turn_right(power_val)
    else:
        fc.stop()
    if key=='q':
        print("quit")  
        break

try:
    client, clientInfo = s.accept()
    while 1:   
#         print("server recv from: ", clientInfo)
        data = client.recv(size)
        if data:
            print(data)
            send_data = "Temperature: " + measure_temp() + " Battery: " + measure_battery()
            client.send(send_data) 
            car_movement(data)
#             client.send(data) # Echo back to client

except: 
    print("Closing socket")
    client.close()
    s.close()

