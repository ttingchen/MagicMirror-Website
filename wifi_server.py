import socket
import picar_4wd as fc
from picar_4wd.utils import pi_read
from remote_control import Remote_control
import json

HOST = "192.168.137.81" # IP address of your Raspberry PI
PORT = 65432          # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    try:
        while 1:
            # gs_list = fc.get_grayscale_list()
            client, clientInfo = s.accept()
            print("server recv from: ", clientInfo)
            data = client.recv(1024)      # receive 1024 Bytes of message in binary format
            result=pi_read()
            if data != b"":
                Remote_control("stop")
                if data == b"forward\r\n":
                    Remote_control("forward")
                    result["car_direction"] = "forward"
                elif data == b"backward\r\n":
                    Remote_control("backward")
                    result["car_direction"] = "backward"
                elif data == b"left\r\n":
                    Remote_control("turn_left")
                    result["car_direction"] = "left"
                elif data == b"right\r\n":
                    Remote_control("turn_right")
                    result["car_direction"] = "right"
                print(data) 
                pidata = json.dumps(result)  
                client.sendall(bytes(pidata,encoding="utf-8")) # Echo back to client
    except: 
        print("Closing socket")
        Remote_control("stop")
        client.close()
        s.close()    
