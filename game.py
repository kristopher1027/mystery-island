"""Game logic for Mystery Island. No input() or print() in this file."""


def new_game(name):
    """Create a fresh game state for a new player."""
    return {
        "name": name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "game_over": False,
        "won": False,
    }


def describe_location(player):
    """Return a description of the player's current location."""
    descriptions = {
        "Beach": "Sandy shore. Path north to the Jungle.",
        "Jungle": "Dense vines. A Cave to the north, Beach to the south.",
        "Cave": "Dark cave. A Lantern lies here. Old Bridge to the north.",
        "Old Bridge": "A rickety rope bridge. Lighthouse to the north.",
        "Lighthouse": "The dark lighthouse. A beacon waits to be lit.",
    }
    return descriptions.get(player["location"], "Unknown place.")


def show_inventory(player):
    """Return a short string listing the player's items."""
    if not player["inventory"]:
        return "Inventory: (empty)"
    return "Inventory: " + ", ".join(player["inventory"])


def available_actions(player):
    """Return a list of actions legal at the player's current location."""
    loc = player["location"]
    actions = []

    if loc == "Beach":
        actions.append("go_jungle")
    elif loc == "Jungle":
        actions.extend(["go_cave", "go_beach"])
    elif loc == "Cave":
        if "rope" not in player["inventory"]:
            actions.append("take_rope")
        if "lantern" not in player["inventory"]:
            actions.append("take_lantern")
        actions.extend(["go_bridge", "go_beach"])
    elif loc == "Old Bridge":
        actions.extend(["go_lighthouse", "go_cave"])
    elif loc == "Lighthouse":
        actions.append("light_beacon")

    actions.append("quit")
    return actions


def _move(player, new_location):
    """Helper: apply a legal move. Deducts 1 energy, ends game at 0."""
    player["location"] = new_location
    player["energy"] -= 1
    if player["energy"] <= 0:
        player["energy"] = 0
        player["game_over"] = True
        player["won"] = False
        return "You collapse from exhaustion. Game over."
    return f"You move to the {new_location}."


def apply_action(player, action):
    """Apply an action to the player state. Returns a message string."""
    if player["game_over"]:
        return "The game is over."

    loc = player["location"]

    if action == "go_jungle" and loc == "Beach":
        return _move(player, "Jungle")
    if action == "go_beach" and loc == "Jungle":
        return _move(player, "Beach")
    if action == "go_cave" and loc == "Jungle":
        return _move(player, "Cave")
    if action == "go_beach" and loc == "Cave":
        return _move(player, "Jungle")
    if action == "go_bridge" and loc == "Cave":
        if "rope" not in player["inventory"]:
            return "The bridge is out. You need rope to cross."
        return _move(player, "Old Bridge")
    if action == "go_cave" and loc == "Old Bridge":
        return _move(player, "Cave")
    if action == "go_lighthouse" and loc == "Old Bridge":
        return _move(player, "Lighthouse")

    if action == "take_rope" and loc == "Cave":
        if "rope" in player["inventory"]:
            return "You already have the rope."
        player["inventory"].append("rope")
        return "You pick up a coil of rope."
    if action == "take_lantern" and loc == "Cave":
        if "lantern" in player["inventory"]:
            return "You already have the lantern."
        player["inventory"].append("lantern")
        return "You pick up a dusty lantern."

    if action == "light_beacon" and loc == "Lighthouse":
        if "lantern" not in player["inventory"]:
            return "It's too dark. You need a lantern."
        player["won"] = True
        player["game_over"] = True
        return "The beacon blazes to life! A rescue boat is coming!"

    if action == "quit":
        player["game_over"] = True
        player["won"] = False
        return "You gave up. Game over."

    return "You can't do that here."


def is_win(player):
    """Return True if the player has won."""
    return player["won"]