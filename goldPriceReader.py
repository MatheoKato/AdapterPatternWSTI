import datetime



class GoldPriceReader():
    def __init__(self):
        self.path = "prices.txt"
        self.prices = dict()

    def get_prices(self):
        date = str(datetime.date.today())
        file = open(self.path, "r", encoding="utf-8")
        for line in file:
            data = line.split(":")
            if date == data[0]:
                self.prices[data[0]] = data[1].strip()
        file.close()
        if self.prices:
            return self.prices
        else:
            return "Nie ma ceny złota z dzisiejszego dnia, proszę sprawdź jutro"









