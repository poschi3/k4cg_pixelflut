from PIL import Image
import threading
import random

class Picture(threading.Thread):
    def __init__(self, verbindung):
        threading.Thread.__init__(self)
        self.pixel = verbindung.pixel
        self.cache = None

    def setPicture(self, name, startx=0, starty=0, width=200, strategie="links_rechts"):
        self.startx = startx
        self.starty = starty
        self.strategie = strategie
        im = Image.open(name).convert('RGBa')
        left, upper, right, lower = im.getbbox()
        height = right / width * lower
        im.thumbnail((width, height), Image.ANTIALIAS)
        self.im = im

    def run(self):
        while True:
            method = getattr(self, "strategie_" + self.strategie, lambda: "nothing")
            method(self.im, self.startx, self.starty)

    def strategie_links_rechts(self, im, startx, starty):
        _, _, w, h = im.getbbox()
        for x in range(w):
            for y in range(h):
                r, g, b, a = im.getpixel((x, y))
                if a != 0:
                    self.pixel(startx + x, starty + y, r, g, b)

    def strategie_rechts_links(self, im, startx, starty):
        _, _, w, h = im.getbbox()
        for x in range(w - 1, 0, -1):
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
        for y in range(h - 1, 0, -1):
            for x in range(w):
                r, g, b, a = im.getpixel((x, y))
                if a != 0:
                    self.pixel(startx + x, starty + y, r, g, b)

    def strategie_pseudo_random(self, im, startx, starty):
        _, _, w, h = im.getbbox()
        if self.cache is None:
            print("Cache leer")
            self.cache = []
            for x in range(w):
                for y in range(h):
                    self.cache.append((x, y))
            random.shuffle(self.cache)
            print("Cache voll")

        for x, y in self.cache:
            r, g, b, a = im.getpixel((x, y))
            if a != 0:
                self.pixel(startx + x, starty + y, r, g, b)
