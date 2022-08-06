"""
A shop needs an iterable object to keep track of product expiration dates.
Each product in the shop will have a string name, datetime expiration date and quantity
Iterating the object will return all products in the shop ordered by expiration date
1) 40p: Definition
    a) 10p: Basic class structure of objects
    b) 10p: Basic class structure of iterator
    b) 10p: Method to add product to the shop
    c) 10p: Method to decrease quantity and remove product
2) 40p: Execution:
    a) 10p: Create instance of your shop
    b) 10p: Add products:
        - Banana, 1 Aug 2022, 100
        - Orange, 2 Aug 2022, 200
        - Orange, 3 Aug 2022, 50
    c) 10p: Remove products
        - Orange, 10
        - Banana, 50
    d) 10p: Iterate the created object.
3) 20p: Documenting:
   a) 5p: type hints for arguments
   a) 5p: module documentation
   b) 5p: class documentation for all classes
   c) 5p: method documentation for all methods
"""


import time
import datetime
#import librarii pentru date si timp

class Magazin:
#clasa pentru magazin
    magazin = {}

    def __init__(self,day:float):
        self.day = datetime.datetime.now()

    def __iter__(self):
        return Iterator(self.magazin)

    def add_cantitate(self,name:str, cantitate:int):
        #clasa pentru adaugarea cantitatii
        self.cantitate=cantitate
        self.magazin[name]=[int(cantitate)]
        return self.magazin[name]


    def add_date(self, name:str, data_expirare:str):
        #clasa pentru adaugarea produsului si al datii*
        year,month, day = data_expirare.split(":")
        self.magazin[name].append( [datetime.datetime(
            year=int(year), month=int(month), day=int(day))])

        return self.magazin[name]


    def update_produs(self,name:str,cantitate:int):
    #clasa pentru adaugarea sau scadere de produse
        self.magazin[name][0] = self.magazin[name][0] - int(cantitate)

        return self.magazin
class Iterator():
#clasa iteratorului
    cos = []

    def __init__(self, cos: dict):
        self.cos = cos
        for produs ,caracteristici in self.cos.items():
            print(produs,caracteristici)

    def __iter__(self):
        return self
    #functia de iterare
    def __next__(self):
        if not self.cos:
            raise StopIteration
        return self.cos.pop()
    #functia next
k=Magazin(time.time())
print(k.add_cantitate("mere",30))
print(k.add_date("mere","2022:05:05"))



print(k.update_produs("mere",29))

print(k.add_cantitate("banana",100))
print(k.add_date("banana","2022:05:05"))
print(k.add_cantitate("orange",100))
print(k.add_date("orange","2022:05:05"))
