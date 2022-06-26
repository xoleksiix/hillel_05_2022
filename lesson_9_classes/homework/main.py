from typing import Union

rate = {"UAH": 0.034, "USD": 1, "EUR": 1.06, "GBP": 1.23}


class Price:
    def __init__(self, amount: Union[int, float], currency: str) -> None:
        self.amount: int = amount
        self.currency: str = currency

    def __str__(self) -> str:
        return f'Price({self.amount}, "{self.currency}")'

    def __add__(self, other: Union["Price", int, float]) -> "Price":
        return self.add_or_sub(other, 1)

    def __sub__(self, other: Union["Price", int, float]) -> "Price":
        return self.add_or_sub(other, -1)

    def add_or_sub(self, other: Union["Price", int, float], index: bool) -> "Price":
        if isinstance(other, (int, float)):
            return Price(self.amount + (index * other), self.currency)
        elif self.currency == other.currency:
            return Price(self.amount + (index * other.amount), self.currency)
        else:
            amount_1 = (
                self.amount
                if self.currency == "USD"
                else self.amount * rate.get(self.currency)
            )
            amount_2 = (
                other.amount
                if other.currency == "USD"
                else other.amount * rate.get(other.currency)
            )
            return Price(
                (amount_1 + (index * amount_2)) * (1 / rate.get(self.currency)),
                self.currency,
            )
            #  ans in left currency ^^^ or USD
            # return Price((amount_1 + (index * amount_2)), self.currency)

    def __mul__(self, other: Union[int, float]) -> "Price":
        return Price(self.amount * other, self.currency)


if __name__ == "__main__":
    # a0 = Price(100, "UAH")
    # b0 = 1.5
    # print(a0 * b0)

    # a1 = Price(100, "UAH")
    # b1 = 200
    # print(a1 + b1)

    # a1 = Price(100, "UAH")
    # b1 = 200
    # print(a1 - b1, "-")

    # a2 = Price(111, "UAH")
    # b2 = Price(222, "UAH")
    # print(a2 + b2)

    # a3 = Price(100, "UAH")
    # b3 = Price(100, "USD")
    # print(a3 - b3, "!")

    # a4 = Price(100, "USD")
    # b4 = Price(100, "UAH")
    # print(a4 + b4)

    # a5 = Price(100, "EUR")
    # b5 = Price(100, "UAH")
    # print(a5 + b5)
