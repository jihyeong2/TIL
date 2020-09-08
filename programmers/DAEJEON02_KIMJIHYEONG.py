import socket
import time
import math

# User and Launcher Information
NICKNAME = 'DAEJEON02_KIMJIHYEONG'
HOST = '127.0.0.1'

# Static Value(Do not modify)
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# Predefined Variables(Do not modify)
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]


class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: %s:%d' % (HOST, PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: %s:%d' % (HOST, PORT))
        send_data = '%d/%s/' % (CODE_SEND, NICKNAME)
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play!\n--------------------')

    def request(self):
        self.sock.send('%d/%d' % (CODE_REQUEST, CODE_REQUEST).encode())
        print('Received Data has been currupted, Resend Requested.')

    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: %s' % recv_data)
        return recv_data

    def send(self, angle, power):
        if power <= 0:
            print('Power must be bigger than 0, Try again.')
            return False
        merged_data = '%f/%f/' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: %s' % merged_data)

    def close(self):
        self.sock.close()
        print('Connection Closed.\n--------------------')


class GameData:
    def __init__(self):
        self.order = 0
        self.reset()

    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = int(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)

    def arrange(self):
        self.order = self.balls[0][1]
        print('\n* You will be the %s player. *\n' %
              ('first' if self.order == 1 else 'second'))

    def show(self):
        print('====== Arrays ======')
        for i in range(NUMBER_OF_BALLS):
            print('Ball %d: %d, %d' % (i, self.balls[i][0], self.balls[i][1]))
        print('====================')


def play(conn, gameData):
    angle = 0.0
    power = 0.0

    ##############################
    # Begining of Your Code
    # Put your code here to set angle and power values.
    # angle(float) must be between 0.0 and 360.0
    # power(float) must be between 0.0 and 100.0
    whiteBall_x = gameData.balls[0][0]
    whiteBall_y = gameData.balls[0][1]
    if gameData.order==1:
        targetBall_x = -1
        targetBall_y = -1
        for i in range(3,0,-2):
            targetBall_x = gameData.balls[i][0]
            targetBall_y = gameData.balls[i][1]
            if targetBall_x!=-1 or targetBall_y!=-1: break
        if targetBall_x==-1 and targetBall_y==-1:
            targetBall_x = gameData.balls[5][0]
            targetBall_y = gameData.balls[5][1]
        width = abs(targetBall_x - whiteBall_x)
        height = abs(targetBall_y - whiteBall_y)
        if width!=0 and height!=0:
            radian = math.atan(width / height)
            distance = math.sqrt(width**2 + height**2)
            angle = 180 / math.pi * radian
            if targetBall_y>whiteBall_y:
                if targetBall_x>whiteBall_x:
                    angle=angle
                else:
                    angle = 360.0-angle
            else:
                if targetBall_x>whiteBall_x:
                    angle = 180.0-angle
                else:
                    angle = 180.0+angle
            power = distance
        else:
            if width==0:
                if targetBall_y>whiteBall_y:
                    angle=0.0
                else:
                    angle=180.0
            if height==0:
                if targetBall_x>whiteBall_x:
                    angle=90.0
                else:
                    angle=270.0
            power=50.0
    else:
        targetBall_x = -1
        targetBall_y = -1
        for i in range(2, 5, 2):
            targetBall_x = gameData.balls[i][0]
            targetBall_y = gameData.balls[i][1]
            if targetBall_x != -1 or targetBall_y != -1: break
        if targetBall_x == -1 and targetBall_y == -1:
            targetBall_x = gameData.balls[5][0]
            targetBall_y = gameData.balls[5][1]
        width = abs(targetBall_x - whiteBall_x)
        height = abs(targetBall_y - whiteBall_y)
        if width != 0 and height != 0:
            radian = math.atan(width / height)
            distance = math.sqrt(width ** 2 + height ** 2)
            angle = 180 / math.pi * radian
            if targetBall_y > whiteBall_y:
                if targetBall_x > whiteBall_x:
                    angle = angle
                else:
                    angle = 360.0 - angle
            else:
                if targetBall_x > whiteBall_x:
                    angle = 180.0 - angle
                else:
                    angle = 180.0 + angle
            power = distance
        else:
            if width == 0:
                if targetBall_y > whiteBall_y:
                    angle = 0.0
                else:
                    angle = 180.0
            if height == 0:
                if targetBall_x > whiteBall_x:
                    angle = 90.0
                else:
                    angle = 270.0
            power = 50.0
        angle-=0.1
        power+=5
    # 선 후 일때 나누어 주었고 아크탄젠트를 이용하여 잰 각도에 타겟좌표와 흰공좌표와의 상관관계에 따라
    # angle 값을 조정하였다.
    # 후순일때는 어림잡아 angle과 power를 조정하였다.

    # You can clear Stage 1 with the pre-written code above.
    # Those will help you to figure out how to clear other Stages.
    # Good luck!!
    # End of Your Code
    ##############################

    conn.send(angle, power)


def main():
    conn = Conn()
    gameData = GameData()
    while True:
        gameData.read(conn)
        if gameData.balls[0][0] == SIGNAL_ORDER:
            gameData.arrange()
            continue
        elif gameData.balls[0][0] == SIGNAL_CLOSE:
            break
        gameData.show()
        play(conn, gameData)

    conn.close()


if __name__ == '__main__':
    main()
