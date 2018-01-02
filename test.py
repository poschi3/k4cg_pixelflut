#!/usr/bin/env python

from verbindung import Verbindung
from picture import Picture
from simpleconfig import SimpleConfig
from size import Size

import sys


config = SimpleConfig().load("config.yml")
size = Size().detect(config.getServerHost(), config.getServerPort())

def k4cg(config, size):
    print("  " + config.getStrategy())
    v = Verbindung(config.getServerHost(), config.getServerPort(), size.width, size.height)
    p = Picture(v)
    p.setPicture(config.getImageFilePath(), config.getDrawPositionX(), config.getDrawPositionY(), config.getDrawWidth(), config.getStrategy())
    if config.useColorBasedImageTransparency():
        p.setColorBasedTransparency(config.getImageTransparencyColor())
    p.start()


#strategies = ['links_rechts', 'rechts_links', 'oben_unten', 'unten_oben', 'pseudo_random']
strategies = ['pseudo_random']

anzahl = 0
while True:
    k4cg(config, size)
    anzahl += 1
    print("Anzahl: " + str(anzahl))
