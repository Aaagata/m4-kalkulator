import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
print("Witaj, ten oto mini-kalkulator wykona wybrane przez Ciebie działanie na dwóch elementach.")
dzialanie = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:\n")
el1 = int(input("Podaj pierwszy element działania: "))
el2 = int(input("Podaj drugi element działania: "))
def kalk(dzialanie, el1, el2):
    if dzialanie == '1':
        print(el1 + el2)
    if dzialanie == '2':
        print(el1 - el2)
    if dzialanie == '3':
        print(el1 * el2)
    if dzialanie == '4':
        print(el1 / el2)
kalk(dzialanie, el1, el2)
print(dzialanie)