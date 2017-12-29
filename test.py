import socket
import _thread
import random
import sys

from PIL import Image

HOST = '151.217.47.77'
PORT = 8080
MAX_X = 800
MAX_Y = 600

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


#def rect(x, y, w, h, r, g, b):
#    for i in range(x, x + w):
#        for j in range(y, y + h):
#            pixel(i, j, r, g, b)




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
            if x > MAX_X:
                x = MAX_X
            if y < 0:
                y = 0
            if y > MAX_Y:
                y = MAX_Y



    def pic(self, name, startx=0, starty=0, width = 200, strategie = "links_rechts"):
        im = Image.open(name).convert('RGBa')
        left, upper, right, lower = im.getbbox()

        height = right / width * lower


        im.thumbnail((width, height), Image.ANTIALIAS)
        #im.convert('RGB')

        method = getattr(self, "strategie_" + strategie, lambda: "nothing")
        # Call the method as we return it
        return method(im, startx, starty)
        #self.strategie_unten_oben(im, startx, starty)

    def strategie_links_rechts(self, im, startx, starty):
        _, _, w, h = im.getbbox()
        for x in range(w):
            for y in range(h):
                r, g, b, a = im.getpixel((x, y))
                if a != 0:
                    self.pixel(startx + x, starty + y, r, g, b)

    def strategie_rechts_links(self, im, startx, starty):
        _, _, w, h = im.getbbox()
        for x in range(w-1, 0, -1):
            for y in range(h):
                r, g, b, a = im.getpixel((x, y))
                if a != 0:
                    self.pixel(startx + x, starty + y, r, g, b)

    def strategie_oben_unten(self, im, startx, starty):
        _, _, w, h = im.getbbox()
        for y in range(h):
            for x in range(w):
                r, g, b, a = im.getpixel((x, y))
                if a != 0:
                    self.pixel(startx + x, starty + y, r, g, b)

    def strategie_unten_oben(self, im, startx, starty):
        _, _, w, h = im.getbbox()
        for y in range(h-1, 0, -1):
            for x in range(w):
                r, g, b, a = im.getpixel((x, y))
                if a != 0:
                    self.pixel(startx + x, starty + y, r, g, b)

def k4cg(strategie = 0):
    t = Verbindung(HOST, PORT, MAX_X, MAX_Y)
    while True:
        t.pic('Logo_leiter.png', 100, 60, 600, strategie)

strategie = sys.argv[1]
print(strategie)
k4cg(strategie)

#try:
#_thread.start_new_thread( k4cg, (None,))

#except:
#   print ("Error: unable to start thread")




#worm(200, 200, 500000, 255, 192, 203)