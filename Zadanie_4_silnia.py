#!/usr/bin/python3

def silnia(n):
    if n == 0:
        return 1
    elif n>0:
        return n*silnia(n-1)
    else:
        return False
    
x = int(input("podaj indeks do obliczenia silni:"))
print("silnia(", x, ") =",silnia(x))
    
    
    


