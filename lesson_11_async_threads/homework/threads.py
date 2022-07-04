import random
from threading import Thread
from typing import Union

random_int = []


def random_numbers():
    for i in range(10_000):
        random_int.append(random.randint(0, 10000))


def sum(x: list) -> int:
    count = 0
    for i in x:
        count += i
    print(count)


def avarage(x: list) -> Union[int, float]:
    count = 0
    for i in x:
        count += i
    print(count / len(x))


def main():
    t1 = Thread(target=random_numbers)
    t1.start()
    t1.join()
    t2 = Thread(target=sum, args=(random_int,))
    t3 = Thread(target=avarage, args=(random_int,))
    t2.start()
    t3.start()
    t2.join()
    t3.join()


if __name__ == "__main__":
    main()
