#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ~/python/04_1_listy.py

tupla = input("Podaj liczby oddzielone przecinkami: ")
lista = []
for i in range(len(tupla)):
    lista.append(int(tupla[i]))

print "Elementy i indeksy ich:"
for i, v in enumerate(lista):
    print v, "[",i,"]"

print "Elementy w odwr�conym porz�dku:"
for e in reversed(lista):
    print e,

print ""
print "Elementy posortowane rosn�co:"
for e in sorted(lista):
    print e,

print ""
e = int(raw_input("Kt�r� liczb� usun��? "))
lista.remove(e)
print lista

a, i = input("Podaj element do dodania i indeks, przed kt�rym ma si� on znale��: ")
lista.insert(i, a)
print lista

e = int(raw_input("Podaj liczb�, kt�rej wyst�pienia w li�cie chcesz zliczy�? "))
print lista.count(e)
print "Pierwszy indeks, pod kt�rym zapisana jest podana liczba to: "
print lista.index(e)

print "Pobieramy ostatni element z listy: "
print lista.pop()
print lista

i, j = input("Podaj indeks pocz�tkowy i ko�cowy, aby uzyska� frgament listy: ")
print lista[i:j]