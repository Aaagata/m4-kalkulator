import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
print("Witaj, ten oto mini-kalkulator wykona wybrane przez Ciebie działanie na dwóch elementach.")
dzialanie = int(print(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:\n")))
el_1 = int(print((input("podaj pierwszy element")))
el_2 = int(print((input("podaj drugi element")))
    
def kalk(dzialanie, el_1, el_2):
    if dzialanie == '1':
        return(el_1 + el_2)
    if dzialanie == 2:
        return(el_1 - el_2)
    if dzialanie == 3:
        return(el_1 * el_2)
    if dzialanie == 4:
        return(el_1 / el_2)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        exit(1)
    el_1 = sys.argv[2]
    el_2 = sys.argv[3]
    dzialanie = sys.argv[1]
    kalk(dzialanie, el_1, el_2)