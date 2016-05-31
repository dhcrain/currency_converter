

class Money:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    @property
    def to_usd(self):
        # amount * xxx_usd = $1
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
        return "{} {}".format(self.amount, "USD")

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


