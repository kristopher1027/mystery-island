"""CLI entry point for Mystery Island."""

from game import (
    new_game,
    describe_location,
    show_inventory,
    apply_action,
    available_actions,
)


def play_once():
    """Play one full session. Returns the final player dict."""
    print("=== MYSTERY ISLAND: The Lost Lighthouse ===")
    print("You wake on a storm-wrecked beach. Restore the beacon or run out of energy.")
    name = input("Enter your name: ").strip()
    if not name:
        name = "Explorer"

    player = new_game(name)

    while not player["game_over"]:
        print()
        print(describe_location(player))
        print(f"Energy: {player['energy']} | Location: {player['location']}")
        print(show_inventory(player))

        actions = available_actions(player)
        print("Actions:")
        for i, a in enumerate(actions, start=1):
            print(f"  {i}. {a}")

        raw = input("> ").strip().lower()
        if not raw:
            print("Invalid choice.")
            continue

        try:
            idx = int(raw) - 1
            if 0 <= idx < len(actions):
                action = actions[idx]
            else:
                print("Invalid choice.")
                continue
        except ValueError:
            if raw in actions:
                action = raw
            else:
                print("Invalid choice.")
                continue

        msg = apply_action(player, action)
        print(msg)

    if player["won"]:
        print(f"\n🏆 {player['name']}, you lit the beacon and were rescued!")
    else:
        print(f"\n💀 {player['name']}, your journey ends here.")
    return player


def main():
    """Run the game, offering replay."""
    while True:
        play_once()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()