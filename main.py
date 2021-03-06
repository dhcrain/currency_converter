

class Money:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    @property
    def to_usd(self):

        rates = {"JPY": 0.009031,
                 "EUR": 1.113634,
                 "BTC": 529.72,
                 "USD": 1
                 }

        if self.currency not in rates.keys():
            print(" ! {} is not compatable with the program ! \n".format(self.currency))
        else:
            return self.amount * rates[self.currency]

    def __str__(self):
        return "{} {}".format(self.amount, self.currency)

    def __eq__(self, other):
        return self.to_usd == other.to_usd

    def __ne__(self, other):
        return self.to_usd != other.to_usd

    def __le__(self, other):
        return self.to_usd <= other.to_usd

    def __lt__(self, other):
        return self.to_usd < other.to_usd

    def __gt__(self, other):
        return self.to_usd > other.to_usd

    def __ge__(self, other):
        return self.to_usd >= other.to_usd

    def __add__(self, other):
        return Money((self.to_usd + other.to_usd), self.currency)

    def __mul__(self, other):
        return Money((self.to_usd * other.to_usd), self.currency)

    def __sub__(self, other):
        return Money((self.to_usd - other.to_usd), self.currency)


btc = Money(1, "BTC")
eur = Money(56.32, "EUR")
jpy = Money(10000, "JPY")
usd = Money(529.72, "USD")
usd2 = Money(8, "USD")

print("All Results in USD")
print("BTC - USD:", btc - usd)
print("EUR * JPY:", eur * jpy)
print("EUR + BTC:", eur + btc)
print("BTC > USD:", btc > usd)
print("EUR >= JPY", eur >= jpy)
print("JPY < BTC", jpy < btc)
print("USD <= USD2", usd <= usd2)
print("JPY != BTC", jpy != btc)
print("BTC == USD", btc == usd)

print(btc.to_usd)
print(eur.to_usd)
print(jpy.to_usd)
print(usd.to_usd)

print(Money(100.00, "USD") + Money(56.32, "EUR") + Money(1.2, "BTC") + Money(8, "USD"))
