

class Money:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    @property
    def to_usd(self):
        jpy_usd = 0.009031
        eur_usd = 1.113634
        btc_usd = 529.72
        if self.currency == "JPY":
            return self.amount * jpy_usd
        elif self.currency == "EUR":
            return self.amount * eur_usd
        elif self.currency == "BTC":
            return self.amount * btc_usd
        else:   # USD
            return self.amount

    def __str__(self):
        return "{} {}".format(self.amount, self.currency.upper())

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
eur = Money(1, "EUR")
jpy = Money(1, "JPY")
usd = Money(1, "USD")

# print("All Results in USD")
# print("BTC - USD:", btc - usd)
# print("EUR * JPY:", eur * jpy)
# print("EUR + BTC:", eur + btc)
# print("BTC > USD:", btc > usd)
# print("EUR >= JPY", eur >= jpy)
# print("JPY < BTC", jpy < btc)

print(btc.to_usd)
print(eur.to_usd)
print(jpy.to_usd)
print(usd.to_usd)
print(Money(100.00, "USD") + Money(56.32, "EUR") + Money(1.2, "BTC") + Money(8, "USD"))


print(100 + 62.70 + 625.98 + 8)
