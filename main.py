

class Money:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

# Implement the conversion rates for USD, JPY, EUR, and BTC.
# 1 usd = 110.74 JPY / JPY to usd 0.009031
# 1 usd = 0.90 EUR / eur to usd 1.113634
# 1 usd = 0.0019 BTC / btc to usd 529.72

    def to_usd(self, amount, currency):
        jpy_usd = 0.009031
        eur_usd = 1.113634
        btc_usd = 529.72
        if currency == "JPY":
            return amount * jpy_usd
        elif currency == "EUR":
            return amount * eur_usd
        elif currency == "BTC":
            return amount * btc_usd
        else:
            return amount

    def __str__(self):
        return "{} {}".format(self.amount, self.currency.upper())

    def __eq__(self, other):
        return self.to_usd(self.amount, self.currency) == other.to_usd(other.amount, other.currency)

    def __ne__(self, other):
        return self.to_usd(self.amount, self.currency) != other.to_usd(other.amount, other.currency)

    def __le__(self, other):
        return self.to_usd(self.amount, self.currency) <= other.to_usd(other.amount, other.currency)

    def __lt__(self, other):
        return self.to_usd(self.amount, self.currency) < other.to_usd(other.amount, other.currency)

    def __gt__(self, other):
        return self.to_usd(self.amount, self.currency) > other.to_usd(other.amount, other.currency)

    def __ge__(self, other):
        return self.to_usd(self.amount, self.currency) >= other.to_usd(other.amount, other.currency)

    def __add__(self, other):
        return self.to_usd(self.amount, self.currency) + other.to_usd(other.amount, other.currency)

    def __mul__(self, other):
        return self.to_usd(self.amount, self.currency) * other.to_usd(other.amount, other.currency)

    def __sub__(self, other):
        return self.to_usd(self.amount, self.currency) - other.to_usd(other.amount, other.currency)


btc = Money(11, "BTC")
eur = Money(333, "EUR")
jpy = Money(20000, "YPY")
usd = Money(100, "USD")

print("All Results in USD")
print("BTC - USD:", btc - usd)
print("EUR * JPY:", eur * jpy)
print("EUR + BTC:", eur + btc)
print("BTC > USD:", btc > usd)
>=print(EUR )
<
<=
!=
==


