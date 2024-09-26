
import unittest

def modul(a):
    if (a>=0):
        return a
    else:
        return -a


def toTroichn(a):
    string = ''
    while a > 0:
        string+=str(a%3)
        a//= 3 
    return(string[::-1])
    

def toNrichn(a, n):
    string = ''
    while a > 0:
        string+=str(a%n)
        a//= n 
    return(string[::-1])
    
def ostatok(a,b):
   return a-(a//b)*b
   
def fromTroichn(a):
    result = 0
    c = 1
    while a!=0:
        result +=ostatok(a,10)*c
        c = c*3
        a = a//10
    return result
    
def fromNrichn(a,n):
    result = 0
    c = 1
    while a!=0:
        result +=ostatok(a,10)*c
        c = c*n
        a = a//10
    return result
    
