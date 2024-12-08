class Auto:
    def __init__(self, kolor, wiek):
        self.kolor = kolor
        self.ilosc_paliwa = 10
        self.kondycja = 5
        self.tryb_ekonimiczny = False
        self.spalanie_na_100 = 14
        self.rocznik = 2024 - wiek

    def zasieg(self):
        zasieg = self.ilosc_paliwa / self.spalanie_na_100 * 100 * 0.9
        return round(zasieg)



car1 = Auto('red', 12)
car2 = Auto('blue', 1)

print(car1.rocznik)
car1.rocznik = 2004
print(car1.rocznik)

print(car2.ilosc_paliwa)
print(car2.zasieg())

