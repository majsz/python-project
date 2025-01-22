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
      
    def display(self):
        print("Obiekty w Układzie Słonecznym:")
        for obj in self.objects:
            print(f"Nazwa: {obj.nazwa}, Odległość: {obj.odleglosc}, Masa: {obj.masa}, Okres obiegu: {obj.okresObiegu}")
        
'''
ALGORYTMY SORTOWANIA - BUCKET SORT

dana - określa według której wartości obiektu CiałoNiebieskie sortujemy obiekty UkładuSłonecznego
'''
# rosnąco
def insertionSort(arr, dana):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and dana(key) < dana(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bucketSort(arr, dana):
    if len(arr) < 2:
        return
    noOfbuckets = max(1, int(len(arr) / 2))  

    temp = []
    max_val = dana(arr[0])
    min_val = dana(arr[0])
    for i in arr:
        if dana(i) > max_val:
            max_val = dana(i)
    for i in arr:
        if dana(i) < min_val:
            min_val = dana(i)
            
    rnge = max((max_val - min_val) / noOfbuckets, 1)

    for i in range(noOfbuckets):
        temp.append([])

    for i in range(len(arr)):
        index = int((dana(arr[i]) - min_val) / rnge)
        if index >= noOfbuckets:  
            index = noOfbuckets - 1
        temp[index].append(arr[i])

    for i in range(noOfbuckets):
        temp[i] = insertionSort(temp[i], dana)

    k = 0
    for i in range(noOfbuckets):
        for j in range(len(temp[i])):
            arr[k] = temp[i][j]
            k += 1

    return arr

# malejąco
def bucketSortDesc(arr, dana):
    if len(arr) < 2:
        return
    noOfbuckets = max(1, int(len(arr)))  
    temp = []
    max_val = dana(arr[0])
    min_val = dana(arr[0])
    for i in arr:
        if dana(i) > max_val:
            max_val = dana(i)
    for i in arr:
        if dana(i) < min_val:
            min_val = dana(i)
            
    rnge = max((max_val - min_val) / noOfbuckets, 1)

    for i in range(noOfbuckets):
        temp.append([])

    for i in range(len(arr)):
        index = int((dana(arr[i]) - min_val) / rnge)
        if index >= noOfbuckets: 
            index = noOfbuckets - 1
        temp[index].append(arr[i])

    for i in range(noOfbuckets):
        temp[i] = insertionSortDesc(temp[i], dana)

    k = 0
    for i in range(noOfbuckets - 1, -1, -1):
        for j in range(len(temp[i])):
            arr[k] = temp[i][j]
            k += 1

    return arr

def insertionSortDesc(arr, dana):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Sortowanie malejące
        while j >= 0 and dana(key) > dana(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr



lista = UkladSloneczny()
lista.add("Ziemia", 1, 5.97, 365)
lista.add("Wenus", 0.72, 4.867, 225)
lista.add("Jowisz", 5.2, 1898, 4333)
lista.add("Saturn", 9.58, 568, 10759)
lista.add("Neptun", 30.05, 102.4, 60190)
lista.add("Uran", 19.22, 86.8, 30687)
'''
lista.display()

print("sort masa:")
bucketSortDesc(lista.objects, dana = lambda obj: obj.masa)
lista.display()

print("sort okresObiegu:")
lista.objects=bucketSortDesc(lista.objects, dana = lambda obj: obj.okresObiegu)

lista.display()

print("sort odleglosc:")
bucketSortDesc(lista.objects, dana = lambda obj: obj.odleglosc)

lista.display()
'''
