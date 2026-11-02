# Mystery Island: The Lost Lighthouse

A beginner-friendly Python text-adventure game. You wake on a storm-wrecked
island and must restore the lighthouse beacon to be rescued — before you run
out of energy.

## Prerequisites

- Python 3.10 or newer (developed on 3.12.3)
- No external libraries required — standard library only

Check your version:

    python3 --version

## How to run

From the project root:

    python3 main.py

You will be prompted for your name, then shown a numbered menu of actions.
Type the **number** of the action you want, or the **action name** itself
(e.g. `go_jungle`). Type `quit` (or pick it from the menu) to end the game.

## How to run the tests

    python3 -m unittest discover -s tests -v

You should see 10 tests run and pass.

## Game rules

- You start at the **Beach** with **5 energy** and an empty inventory.
- Each **legal move** costs **1 energy**.
- **Invalid input** costs nothing and changes nothing.
- Locations, in order: **Beach → Jungle → Cave → Old Bridge → Lighthouse**.
- You can go **backwards** (Lighthouse → Old Bridge → Cave → Jungle → Beach).
- The **Cave** contains two items: **rope** and **lantern**. Pick each up once.
- The **Old Bridge** cannot be crossed without the **rope**.
- The **beacon** cannot be lit without the **lantern**.
- Lighting the beacon **wins**. Running out of energy **loses**. Quitting **ends** the game.
- After game over, you may replay with a fresh state.

### Winning path (one example)

1. `go_jungle` (energy 4)
2. `go_cave` (energy 3)
3. `take_rope` (free)
4. `take_lantern` (free)
5. `go_bridge` (energy 2 — requires rope)
6. `go_lighthouse` (energy 1)
7. `light_beacon` → WIN

### Losing path

Bounce between Beach and Jungle five times; energy reaches 0 and the game ends.

## Known limitations

- No save/load — replay always starts a fresh game.
- Single player, terminal only.
- No difficulty settings; energy is fixed at 5.
- The map is linear and small by design (beginner project).
- Invalid input is rejected but not logged.

## File structure

    mystery-island/
    ├── main.py            # interface: input() / print() loop
    ├── game.py            # pure game logic (no I/O)
    ├── tests/test_game.py # 12 unit tests
    ├── README.md
    └── .gitignore

Game logic is fully separated from UI, so tests can call functions without
typing anything.

## Author
CHRISTOPHER OKOH