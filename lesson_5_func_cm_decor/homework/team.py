team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 12},
]


def repr_players(
    players: list[dict], sort_players: bool = False, key: str = "number"
) -> None:
    print("TEAM:")
    if sort_players:
        for player in sorted(players, key=lambda x: x[key]):
            print(
                f"\t{player['number']} \
                Name: {player['name']}, Age: {player['age']}"
            )
    else:
        for player in players:
            print(
                f"\t{player['number']} \
                Name: {player['name']}, Age: {player['age']}"
            )
    print("\n")


def log(message: str) -> None:
    print(f">>> {message} <<<")


def add_player(num: int, name: str, age: int) -> None:
    new_player = {"name": name, "number": num, "age": age}
    if new_player["number"] in [player["number"] for player in team]:
        log(message="Number is being used by other players")
    else:
        team.append(new_player)
        log(message=f"Adding {new_player['name']}")


def remove_player(players: list[dict], num: int) -> None:
    for index, player in enumerate(players):
        if player["number"] == num:
            player_name = player["name"]
            del players[index]
            log(message=f"Deleting {player_name}")


def update_player(players: list[dict], num: int, new_name: str, new_age: int) -> None:
    if num in [player["number"] for player in team]:
        


def main():
    repr_players(team, True, "age")

    add_player(num=17, name="Cris", age=31)
    add_player(num=17, name="Bob", age=39)
    remove_player(players=team, num=17)

    repr_players(team)


if __name__ == "__main__":
    main()
