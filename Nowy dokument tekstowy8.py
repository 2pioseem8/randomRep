#! /usr/bin/env python
# -*- coding: utf-8 -*-

import math  # do��czamy bibliotek� matematyczn�

op = "t"  # deklarujemy i inicjujemy zmienn� pomocnicz�
while op != "n":  # dop�ki warto�� zmiennej op jest inna ni� znak "n"
    a, b, c = input("Podaj 3 boki tr�jk�ta (oddzielone przecinkami): ")
    # a, b, c = [int(x) for x in raw_input("Podaj 3 boki tr�jk�ta (oddzielone spacjami): ").split()]

    if a + b > c and a + c > b and b + c > a:  # warunek z�o�ony
        print "Z podanych bok�w mo�na zbudowa� tr�jk�t."
        # czy boki spe�niaj� warunki tr�jk�ta prostok�tnego?
        if ((a**2 + b**2) == c**2 or (a**2 + c**2) == b**2 or (b**2 + c**2) == a**2):
            print "Do tego prostok�tny!"

        # na wyj�ciu mo�emy wyprowadza� wyra�enia
        print "Obw�d wynosi:", (a + b + c)
        p = 0.5 * (a + b + c)  # obliczmy wsp�czynnik wzoru Herona
        # liczymy pole ze wzoru Herona
        P = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print "Pole wynosi:", P
        op = "n"  # ustawiamy zmienn� na "n", aby wyj�� z p�tli while
    


    else:
        print "Z podanych odcink�w nie da sie utworzy� tr�jk�ta prostok�tnego."
        op = raw_input("Spr�bujesz jeszcze raz (t/n): ")


print "Narazie"