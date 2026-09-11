from goblin import Goblin


ARENA_NAME = "The Gold Le Colleseum"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The beast comes running out..")

    goblin = Goblin("Gus")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    goblin2 = Goblin("scribble")
    
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
    print("But no hero has answered the call... yet.")


if __name__ == "__main__":
    main()
