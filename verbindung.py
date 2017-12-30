import random
import socket

class Verbindung:
    def __init__(self, host, port, maxX, maxY):
        self.host = host
        self.port = port
        self.maxX = maxX
        self.maxY = maxY
        self.sock = None
        self.connect()

    def connect(self):
        if self.sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.host, self.port))
        return self.sock

    def pixel(self, x, y, r, g, b, a=255):
        if a == 255:
            self.sock.send(b'PX %d %d %02x%02x%02x\n' % (x, y, r, g, b))
        else:
            self.sock.send(b'PX %d %d %02x%02x%02x%02x\n' % (x, y, r, g, b, a))

    def plusminus(self):
        number = random.randint(0, 1)
        if number == 0:
            return -1
        else:
            return 1

    def worm(self, x, y, r, g, b):
        while n:
            r = random.randint(0, 254)
            g = random.randint(0, 254)
            b = random.randint(0, 254)

            self.pixel(x, y, r, g, b, 255)
            x += self.plusminus()
            y += self.plusminus()
            if x < 0:
                x = 0
            if x > self.maxX:
                x = self.maxX
            if y < 0:
                y = 0
            if y > self.maxY:
                y = self.maxY
