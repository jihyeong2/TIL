import socket

# User and Launcher Information
NICKNAME = 'DAEJEON02_KIMJIHYEONG'
HOST = '127.0.0.1'

# Static Value(Do not modify)
PORT = 1447

# Predefined Variables(Do not modify)
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [ [0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127] ]

class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: %s:%d' % (HOST, PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: %s:%d' %(HOST, PORT))
        send_data = '9901/' + NICKNAME
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play.\n--------------------')
    def close(self):
        self.sock.close()
        print('Connection Closed')

def main():
    conn = Conn()
    conn.close()

if __name__ == '__main__':
    main()