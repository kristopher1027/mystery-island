# Learning Log — Mystery Island Project

**Author:** [YOUR NAME]
**Python version:** 3.12.3
**Date:** [TODAY'S DATE]
**Project:** Mystery Island: The Lost Lighthouse (interactive Python text adventure)

---

## Learning Log Entry 1

**Topic:** `input()` always returns a string, not a number.

**What AI said:**
The mentor explained that `input()` always gives back a string (`str`), even when the user types a number. To do arithmetic, I must convert the result with `int()` or `float()`. He also explained that quotes decide a value's type: `0` is an integer, but `"0"` is a string. Without conversion, writing `"5" + 1` raises a `TypeError` because you cannot glue a string and a number together.

**My experiment:**
I opened a Python shell and ran:

    x = input("Type 5: ")
    print(type(x))
    y = int(x)
    print(type(y))
    print(x + "0")
    print(y + 0)
    print(f"{x}{y}")

I typed `5`. The output was:

    <class 'str'>
    <class 'int'>
    50
    5
    55

`type(x)` printed `<class 'str'>` and `type(y)` printed `<class 'int'>`. `x + "0"` printed `50` because it glued two strings together. `y + 0` printed `5` because it added two integers. In an earlier drill I had also said `score = 0` was a string — after running this experiment I could see clearly that it is an **int**, because it has no quotes.

**My conclusion:**
I now understand that `input()` never gives me a number directly — it gives me text. If I forget to convert, arithmetic crashes or misbehaves. This is why `main.py` wraps `int(raw)` inside a `try/except ValueError` block: the menu needs a number, but a bad input like `"banana"` must be rejected with a friendly message instead of crashing the game.

---

## Learning Log Entry 2

**Topic:** Why game logic (`game.py`) is kept separate from the user interface (`main.py`).

**What AI said:**
The mentor explained that `game.py` should hold all the rules and **never** call `input()` or `print()`. `main.py` is the only file that talks to the human. That way, the rules can be tested by calling functions directly, without any typing. He also explained that all state changes should happen in one place so that debugging is easy — a wrong rule lives in `game.py`, a wrong menu lives in `main.py`.

**My experiment:**
I ran:

    python -m unittest discover -s tests -v

and watched **12 tests pass without typing anything**. The tests called `apply_action(player, "go_jungle")` directly and checked the result with `assertEqual`. If `game.py` contained `input()`, the tests would hang waiting for the keyboard, and I would never know which rule was broken. I also noticed that all state changes happen in just two functions — `apply_action` and `_move` — so debugging is bounded.

**My conclusion:**
Separating logic from the interface means I can test the game's rules in seconds, without playing the game by hand. When something goes wrong, I know exactly where to look: a rule bug lives in `game.py`, a display bug lives in `main.py`. This is the same pattern real applications use — UI on top, logic underneath — and it makes my code easier to read, test, and fix.

---

## Final Reflection

The concept I understand now that I didn't before is **why `input()` always returns a string, and why that matters**. Before this project, I thought that if I typed `5` into a program, Python would treat it as a number. But in my experiment, `type(x)` printed `<class 'str'>` — it was still text. When I tried `x + "0"`, the result was `50` (text glued together), not the number fifty. That showed me why I have to convert with `int()` before doing arithmetic. Now I understand why `main.py` uses `int(raw)` inside a `try/except` block — the game needs a number to index the menu, but a bad input like `"banana"` must not crash it. This small idea — "input is always text until you convert it" — is the reason my game's menu can safely reject invalid input and redraw instead of crashing.

---

## Evidence Summary

- **Tests:** 12 tests in `tests/test_game.py`, all passing.
- **Command:** `python -m unittest discover -s tests -v`
- **Winning path:** Beach → Jungle → Cave → take rope → take lantern → Bridge → Lighthouse → light beacon → 🏆
- **Losing path:** Beach ↔ Jungle five times → energy reaches 0 → 💀
- **Invalid input:** `banana`, `999`, blank line, `  QUIT  ` — all rejected without crashing and without costing energy.
- **Python version:** 3.12.3