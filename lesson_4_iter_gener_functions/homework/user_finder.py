from typing import Generator

FILENAME = "rockyou.txt"
SEARCH_KEYWORD = "user"


def read_lines_find_user_generator() -> Generator:
    with open(FILENAME) as file:
        while True:
            line = file.readline()
            if not line:
                break
            if SEARCH_KEYWORD in line:
                yield line.replace("\n", "")


def answer(line) -> bool:
    while True:
        quest = input(f"Want to add <<{line}>>? [Y/N]: ")
        if quest.lower() in ["y", "yes"]:
            return True
        elif quest.lower() in ["n", "no", "not"]:
            return False
        else:
            print("Non-correct input. Try again!")


def user_finder():
    results = []
    for line in read_lines_find_user_generator():
        if answer(line):
            results.append(line)
            print(f"{line} added.")
    print(f"Results: {results}.\nAmount of added lines: {len(results)}.")


if __name__ == "__main__":
    user_finder()
