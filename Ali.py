class Bib ():
    def __init__(self,speed,power,health,):
        self.speed=speed
        self.power=power
        self.health=health
    def s(self):
        return self.speed+self.power+self.health

warior=Bib(2,3,4)
mage=Bib(99999999,9999999999,99999999999)
print(warior.s()<mage.s())