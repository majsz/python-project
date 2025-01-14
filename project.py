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


'''
STRUKTURY DANYCH
'''
class CialoNiebieskie():
    def __init__(self, nazwa=None, odleglosc=None, masa=None, okresObiegu=None):
        self.nazwa = nazwa
        self.odleglosc = odleglosc
        self.masa = masa
        self.okresObiegu = okresObiegu

    def edit(self, nazwa=None, odleglosc=None, masa=None, okresObiegu=None):
        if nazwa is not None:
            self.nazwa = nazwa
        if odleglosc is not None:
            self.odleglosc = odleglosc
        if masa is not None:
            self.masa = masa
        if okresObiegu is not None:
            self.okresObiegu = okresObiegu

class UkladSloneczny():
    def __init__(self):
        self.objects = [] 

    def __getitem__(self, index):
        if (index < len(self.objects)):    
            return self.objects[index]
        print("Układ Słoneczny nie zawiera tylu elementów")

    def __setitem__(self, index, value):
        if (index < len(self.objects)):    
            self.objects[index] = value
        print("Układ Słoneczny nie zawiera tylu elementów")
        
    def add(self, nazwa, odleglosc, masa, okresObiegu):
        self.objects.append(CialoNiebieskie(nazwa, odleglosc, masa, okresObiegu))
       
    def remove_by_name(self, nazwa):
        self.objects = [obj for obj in self.objects if obj.nazwa != nazwa]
        
    def edit_by_name(self, doEdytowania, nazwa=None, odleglosc=None, masa=None, okresObiegu=None):
        for obj in self.objects:
            if (obj.nazwa == doEdytowania):
                obj.edit(nazwa, odleglosc, masa, okresObiegu)
                
    def edit_by_position(self, doEdytowania, nazwa=None, odleglosc=None, masa=None, okresObiegu=None):
        if doEdytowania < len(self.objects):
            self[doEdytowania].edit(nazwa, odleglosc, masa, okresObiegu)
        else:
            print("Układ Słoneczny nie zawiera tylu elementów")
                
    def display(self):
        print("Obiekty w Układzie Słonecznym:")
        for obj in self.objects:
            print(f"Nazwa: {obj.nazwa}, Odległość: {obj.odleglosc}, Masa: {obj.masa}, Okres obiegu: {obj.okresObiegu}")
        
'''
ALGORYTMY SORTOWANIA - BUCKET SORT
'''



lista = UkladSloneczny()
lista.add("Słońce", 0,0.2, 0)
lista.add("Ziemia", 11, 5, 365)
lista.display()

lista.edit_by_position(1,masa=123)  
lista.display()
#bucket_sort_descending(lista.objects, dana = lambda obj: obj.masa)

lista.display()