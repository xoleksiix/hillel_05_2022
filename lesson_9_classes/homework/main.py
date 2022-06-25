class Price:
    def __init__(self, amount: int, currency: str) -> None:
        self.amount: int = amount
        self.currency: str = currency

    def __str__(self) -> str:
        return f"Price({self.amount}, {self.currency})"

    def __add__(self, other: "Price") -> "Price":
        pass

    def __sub__(self, other: "Price") -> "Price":
        pass


if __name__ == "__main__":
    a = Price(100, "UAH")
    print(a)
