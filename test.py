import socket

from PIL import Image

HOST = '151.217.47.77'
PORT = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
send = sock.send

MAX_X = 800
MAX_Y = 600


def pixel(x, y, r, g, b, a=255):
    if a == 255:
        send(b'PX %d %d %02x%02x%02x\n' % (x, y, r, g, b))
    else:
        send(b'PX %d %d %02x%02x%02x%02x\n' % (x, y, r, g, b, a))


def rect(x, y, w, h, r, g, b):
    for i in range(x, x + w):
        for j in range(y, y + h):
            pixel(i, j, r, g, b)


import random

def plusminus():
    number = random.randint(0, 1)
    if number == 0:
        return -1
    else:
        return 1


def worm(x, y, n, r, g, b):
    while n:
        r = random.randint(0, 254)
        g = random.randint(0, 254)
        b = random.randint(0, 254)

        pixel(x, y, r, g, b, 255)
        x += plusminus()
        y += plusminus()
        if x < 0:
            x = 0
        if x > MAX_X:
            x = MAX_X
        if y < 0:
            y = 0
        if y > MAX_Y:
            y = MAX_Y
        # n -= 1    im.



def pic(name, startx=0, starty=0, width = 200):
    im = Image.open(name).convert('RGBa')
    left, upper, right, lower = im.getbbox()

    height = right / width * lower


    im.thumbnail((width, height), Image.ANTIALIAS)
    #im.convert('RGB')

    _, _, w, h = im.getbbox()
    for x in range(w):
        for y in range(h):
            #bla = im.getpixel((x, y))
            r, g, b, a = im.getpixel((x, y))
            pixel(startx + x, starty + y, r, g, b)

while True:
    pic('fahrplan.png', 0, 0, 800)
    #pic('fahrplan.png', 300, 300)

#worm(200, 200, 500000, 255, 192, 203)