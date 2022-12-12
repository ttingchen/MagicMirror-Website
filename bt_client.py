import bluetooth
import sys
import tty
import termios
import asyncio

def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return chr(0x10 + ord(c3) - 65)

host = "BC:20:CF:80:CD:90" # The address of Raspberry PI Bluetooth adapter on the server.
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host, port))
while 1:
    text = input("If you want to quit. Please enter quit: ") # Note change to the old (Python 2) raw_input
    if text == "quit":
        break
    key=readkey()
    sock.send(key)

    data = sock.recv(1024)
    print(data)

sock.close()
