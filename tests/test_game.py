import unittest
from game import new_game, apply_action


class TestNewGame(unittest.TestCase):
    def test_starts_at_beach_with_5_energy(self):
        p = new_game("Ada")
        self.assertEqual(p["location"], "Beach")
        self.assertEqual(p["energy"], 5)
        self.assertEqual(p["inventory"], [])
        self.assertFalse(p["game_over"])
        self.assertFalse(p["won"])


class TestMovement(unittest.TestCase):
    def test_invalid_action_changes_nothing(self):
        p = new_game("Ada")
        apply_action(p, "banana")
        self.assertEqual(p["location"], "Beach")
        self.assertEqual(p["energy"], 5)

    def test_legal_move_decreases_energy_once(self):
        p = new_game("Ada")
        apply_action(p, "go_jungle")
        self.assertEqual(p["location"], "Jungle")
        self.assertEqual(p["energy"], 4)

    def test_wrong_direction_rejected(self):
        p = new_game("Ada")
        apply_action(p, "go_cave")
        self.assertEqual(p["location"], "Beach")
        self.assertEqual(p["energy"], 5)


class TestInventory(unittest.TestCase):
    def test_rope_collected_only_once(self):
        p = new_game("Ada")
        apply_action(p, "go_jungle")
        apply_action(p, "go_cave")
        apply_action(p, "take_rope")
        apply_action(p, "take_rope")
        self.assertEqual(p["inventory"].count("rope"), 1)

    def test_bridge_blocked_without_rope(self):
        p = new_game("Ada")
        p["location"] = "Cave"
        apply_action(p, "go_bridge")
        self.assertEqual(p["location"], "Cave")


class TestWinLose(unittest.TestCase):
    def test_lighthouse_not_lit_without_lantern(self):
        p = new_game("Ada")
        p["location"] = "Lighthouse"
        apply_action(p, "light_beacon")
        self.assertFalse(p["won"])
        self.assertFalse(p["game_over"])

    def test_correct_path_wins(self):
        p = new_game("Ada")
        p["location"] = "Lighthouse"
        p["inventory"] = ["lantern"]
        apply_action(p, "light_beacon")
        self.assertTrue(p["won"])
        self.assertTrue(p["game_over"])

    def test_energy_exhaustion_causes_loss(self):
        p = new_game("Ada")
        p["energy"] = 1
        apply_action(p, "go_jungle")
        self.assertTrue(p["game_over"])
        self.assertFalse(p["won"])
        self.assertEqual(p["energy"], 0)


class TestReplay(unittest.TestCase):
    def test_replay_resets_state(self):
        p = new_game("Ada")
        p["inventory"].append("rope")
        p["energy"] = 1
        p2 = new_game("Ada")
        self.assertEqual(p2["energy"], 5)
        self.assertEqual(p2["inventory"], [])
        self.assertEqual(p2["location"], "Beach")


if __name__ == "__main__":
    unittest.main()