import random
import math
import numpy

x = sorted(numpy.random.normal(2,2,2000))

def mediana(wekt):
    if len(wekt)%2 == 0:
        return (wekt[(len(wekt)//2)-1]+wekt[(len(wekt)//2)])/2
    else:
        return wekt[(len(wekt))//2]

print("mediana",mediana(x))

def kwartyle(wekt):
    Q1 = []
    Q3 = []
    Q2 = mediana(wekt)
    for i in wekt:
        if i <= Q2:
            Q1.append(i)
        elif i >= Q2:
            Q3.append(i)
    kwart_1 = mediana(Q1)
    kwart_3 = mediana(Q3)
    return kwart_1, Q2, kwart_3

print("kwartyle",kwartyle(x))


def rozstep_proba(wekt):
    return wekt[len(wekt)-1]-wekt[0]

print("rozstep1",rozstep_proba(x))

def rozstep_kwart(wekt):
    return kwartyle(wekt)[2] - kwartyle(wekt)[0]

print("rozstep2",rozstep_kwart(x))


def wariancja(wekt):
    aryt = 0
    for i in range(len(wekt)):
        aryt += wekt[i]
    aryt = aryt/len(wekt)
    suma = 0
    for i in range(len(wekt)):
        suma+= (wekt[i]-aryt)**2
    return (1/(len(wekt)-1))*suma

print("wariancja",wariancja(x))


def odchylenie(wekt):
    return math.sqrt(wariancja(wekt))

print("odchylenie",odchylenie(x))