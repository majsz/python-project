# -*- coding: utf-8 -*-
"""
PROJEKT 
3. Algorytm sortowania kubełkowego dla obiektów w naszym układzie słonecznym.

Należy napisać aplikację pozwalającą dodawać, edytować, usuwać, a przede wszystkim sortować rzeczywiste 
obiekty w naszym Układzie Słonecznym według: odległości od Słońca, masy, okresu obiegu dookoła Słońca (rosnąco i malejąca). 
Należy zaprojektować odpowiednią strukturę danych do przechowywania informacji o ciele niebieskim oraz strukturę do ich
przechowywania.

Literatura: T.H. Cormen, C.E. Leiserson, R.L. Rivest, "Wprowadzenie do algorytmów," WNT, Warszawa, 2001.
"""

class CialoNiebieskie():
    def __init__(self, nazwa=None, odleglosc=None, masa=None, okresObiegu=None):
        self.nazwa = nazwa
        self.odlegloscarkoar = odleglosc
        self.masa = masa
        self.okresObiegu = okresObiegu
        self.next = None
        
    def edit(self, nazwa=None, odleglosc=None, masa=None, okresObiegu=None):
        if nazwa is not None:
            self.nazwa = nazwa
        if odleglosc is not None:
            self.odleglosc = odleglosc
        if masa is not None:
            self.masa = masa
        if okresObiegu is not None:
            self.okresObiegu = okresObiegu
class List():
    def __init__(self):
        self.head = CialoNiebieskie()
        
    def append(self, nazwa, odleglosc, masa, okresObiegu):
        appended_node = CialoNiebieskie(nazwa, odleglosc, masa, okresObiegu)
        if self.head.nazwa == None:
            self.head = appended_node
        else: 
            counter = self.head
            while(counter.next != None):
                counter=counter.next
            counter.next = appended_node
            
    def display(self):
        counter=self.head
        print(counter.nazwa)
        while counter.next!=None:
              print(counter.next.nazwa + counter.next.odleglosc)
              counter = counter.next
              
    def length(self):
        counter = self.head
        if self.head.nazwa==None:
            return 0
        output = 1
        while counter.next != None:
            counter=counter.next
            output +=1
        return output
    
    def remove(self, node):
        counter=self.head
        while counter.next!=None or counter.next != node:
            counter = counter.next
        if (counter.next == None):
            print("Brak ciała niebieskiego w układzie słonecznym")
            return
        tmp = counter.next
        counter.next = tmp.next
        '''
        EDYTOWANIE - jak ma wygladac? czy mozna lista.edit(planeta, ...wszystkie dane..)
        czy np bierze liczbe - pozycje na liscie i tylko ją edytuje?
        '''
    def edit(self, planeta, nazwa=None, odleglosc=None, masa=None, okresObiegu=None):
        counter = self.head
        while counter is not None:  
            if counter == planeta:  
                counter.edit(nazwa, odleglosc, masa, okresObiegu)
                return
            counter = counter.next
        print("Brak ciała niebieskiego w układzie słonecznym")



lista = List()
lista.append("Słońce", 0,0.2, 0)
lista.append("Ziemia", 11, 5, 365)
lista.display()
counter = lista.head
i = 0
while counter != None:
    if i == 1:
        counter.edit(odleglosc = 23)
    i+=1
    counter=counter.next
    
        
lista.display()
