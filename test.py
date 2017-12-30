from verbindung import Verbindung
from picture import Picture
import sys

HOST = '151.217.47.77'
PORT = 8080
MAX_X = 800
MAX_Y = 600

def k4cg(strategie = 'links_rechts'):
    print("  " + strategie)
    v = Verbindung(HOST, PORT, MAX_X, MAX_Y)
    p = Picture(v)
    p.setPicture('Logo_leiter.png', 100, 60, 600, strategie)
    p.start()


#strategies = ['links_rechts', 'rechts_links', 'oben_unten', 'unten_oben', 'pseudo_random']
strategies = ['pseudo_random']

anzahl = 0
while True:
    k4cg('pseudo_random')
    anzahl += 1
    print("Anzahl: " + str(anzahl))
