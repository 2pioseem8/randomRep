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

print "Elementy w odwróconym porzadku:"
for e in reversed(lista):
    print e,

print ""
print "Elementy posortowane rosnaco:"
for e in sorted(lista):
    print e,

print ""
e = int(raw_input("Które liczbe usunie? "))
lista.remove(e)
print lista

a, i = input("Podaj element do dodania i indeks, przed którym ma siê on znaleŸæ: ")
lista.insert(i, a)
print lista

e = int(raw_input("Podaj liczbê, której wyst¹pienia w liœcie chcesz zliczyæ? "))
print lista.count(e)
print "Pierwszy indeks, pod którym zapisana jest podana liczba to: "
print lista.index(e)

print "Pobieramy ostatni element z listy: "
print lista.pop()
print lista

i, j = input("Podaj indeks pocz¹tkowy i koñcowy, aby uzyskaæ frgament listy: ")
print lista[i:j]
