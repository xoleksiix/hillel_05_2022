from random import choice
from string import ascii_letters


def get_random_string(n: int) -> str:
    return "".join((choice(ascii_letters) for _ in range(n)))


data = [get_random_string(100) for _ in range(10)]
enum_data = enumerate(data)
print(data)
print(enum_data)
# print(len(data))
# print(sys.getsizeof(data))
for i in enum_data:
    print(type(i))
