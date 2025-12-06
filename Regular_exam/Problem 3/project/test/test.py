import unittest
from project.star_system import StarSystem

class SimpleTest(unittest.TestCase):
    def test_name_setter_valid(self):
        s = StarSystem("Solar", "Yellow dwarf", "Single", 5)
        self.assertEqual(s.name, "Solar")

    def test_name_setter_invalid(self):
        with self.assertRaises(ValueError) as text:
            StarSystem("    ", "Red giant", "Single", 5)

        self.assertEqual(
            str(text.exception),
            "Name must be a non-empty string."
        )

    def test_star_type_setter_valid(self):
        s = StarSystem("Solar", "Yellow dwarf", "Single", 5)
        self.assertEqual(s.star_type, "Yellow dwarf")

    def test_star_type_setter_invalid(self):
        with self.assertRaises(ValueError) as text:
            StarSystem("Solar", "Yellow giant", "Single", 5)

        self.assertEqual(
            str(text.exception),
            f"Star type must be one of {sorted(StarSystem._STAR_TYPES)}."
        )

    def test_system_type_setter_valid(self):
        s = StarSystem("Solar", "Yellow dwarf", "Single", 5)
        self.assertEqual(s.system_type, "Single")

    def test_system_type_setter_invalid(self):
        with self.assertRaises(ValueError) as text:
            StarSystem("Solar", "Yellow dwarf", "Double", 5)

        self.assertEqual(
            str(text.exception),
            f"System type must be one of {sorted(StarSystem._STAR_SYSTEM_TYPES)}."
        )

    def test_num_planets_setter_valid(self):
        s = StarSystem("Solar", "Yellow dwarf", "Single", 5)
        self.assertEqual(s.num_planets, 5)

    def test_num_planets_setter_invalid(self):
        with self.assertRaises(ValueError) as text:
            StarSystem("Solar", "Yellow dwarf", "Single", -5)

        self.assertEqual(
            str(text.exception),
            "Number of planets must be a non-negative integer."
        )

    def test_habitable_zone_range_setter_valid_none(self):
        s = StarSystem("Solar", "Yellow dwarf", "Single", 5)
        self.assertEqual(s.habitable_zone_range, None)

    def test_habitable_zone_range_setter_valid(self):
        s = StarSystem("Solar", "Yellow dwarf", "Single",
                       5, (2, 3))

        self.assertEqual(s.habitable_zone_range, (2, 3))

    def test_habitable_zone_range_setter_invalid_exceeds_two_elements(self):
        with self.assertRaises(ValueError) as text:
            StarSystem("Solar", "Yellow dwarf", "Single",
                       5, (1, 2, 3))

        self.assertEqual(
            str(text.exception),
            "Habitable zone range must be a tuple of two numbers (start, end) where start < end."
        )

    def test_habitable_zone_range_setter_invalid_below_two_elements(self):
        with self.assertRaises(ValueError) as text:
            StarSystem("Solar", "Yellow dwarf", "Single",
                       5, (1,))

        self.assertEqual(
            str(text.exception),
            "Habitable zone range must be a tuple of two numbers (start, end) where start < end."
        )

    def test_habitable_zone_range_setter_invalid_start_greater_than_end(self):
        with self.assertRaises(ValueError) as text:
            StarSystem("Solar", "Yellow dwarf", "Single",
                       5, (3, 2))

        self.assertEqual(
            str(text.exception),
            "Habitable zone range must be a tuple of two numbers (start, end) where start < end."
        )

    def test_is_habitable_method_true(self):
        s = StarSystem("Solar", "Yellow dwarf", "Single",
                       5, (2, 4))

        self.assertTrue(s.is_habitable)

    def test_is_habitable_method_false_habitable_zone_range_is_none(self):
        s = StarSystem("Solar", "Yellow dwarf", "Single",5)

        self.assertFalse(s.is_habitable)

    def test_is_habitable_method_false_num_planets_is_zero(self):
        s = StarSystem("Solar", "Yellow dwarf", "Single",
                       0, (2, 4))

        self.assertFalse(s.is_habitable)

    def test_gt_dunder_method_exception_one_system_not_habitable(self):
        s1 = StarSystem("Solar", "Yellow dwarf", "Single",
                       5, (2, 4))

        s2 = StarSystem("Sigma", "Red dwarf", "Single",5)

        with self.assertRaises(ValueError) as text:
            value = s1 > s2

        self.assertEqual(
            str(text.exception),
            "Comparison not possible: One or both systems lack a defined habitable zone or planets."
        )

    def test_gt_dunder_method_exception_both_systems_not_habitable(self):
        s1 = StarSystem("Solar", "Yellow dwarf", "Single",
                       0, (2, 4))

        s2 = StarSystem("Sigma", "Red dwarf", "Single",5)

        with self.assertRaises(ValueError) as text:
            value = s1 > s2

        self.assertEqual(
            str(text.exception),
            "Comparison not possible: One or both systems lack a defined habitable zone or planets."
        )

    def test_gt_dunder_method_system_one_is_greater(self):
        s1 = StarSystem("Solar", "Yellow dwarf", "Single",
                        5, (2, 4))

        s2 = StarSystem("Sigma", "Red dwarf", "Single",
                        5, (2, 3))

        self.assertTrue(s1 > s2)

    def test_gt_dunder_method_system_two_is_greater(self):
        s1 = StarSystem("Solar", "Yellow dwarf", "Single",
                        5, (2, 3))

        s2 = StarSystem("Sigma", "Red dwarf", "Single",
                        5, (2, 5))

        self.assertFalse(s1 > s2)

    def test_compare_star_systems_method_exception(self):
        s1 = StarSystem("Solar", "Yellow dwarf", "Single",
                        0, (2, 4))

        s2 = StarSystem("Sigma", "Red dwarf", "Single", 5)

        self.assertEqual(StarSystem.compare_star_systems(s1, s2),
                         "Comparison not possible: One or both systems lack a defined habitable zone or planets.")

    def test_compare_star_systems_method_system_one_is_greater(self):
        s1 = StarSystem("Solar", "Yellow dwarf", "Single",
                        5, (2, 4))

        s2 = StarSystem("Sigma", "Red dwarf", "Single",
                        5, (2, 3))

        self.assertEqual(StarSystem.compare_star_systems(s1, s2),
                         f"{s1.name} has a wider habitable zone than {s2.name}.")

    def test_compare_star_systems_method_system_two_is_greater(self):
        s1 = StarSystem("Solar", "Yellow dwarf", "Single",
                        5, (2, 3))

        s2 = StarSystem("Sigma", "Red dwarf", "Single",
                        5, (2, 4))

        self.assertEqual(StarSystem.compare_star_systems(s1, s2),
                         f"{s2.name} has a wider or equal habitable zone compared to {s1.name}.")

    def test_compare_star_systems_method_both_are_equal(self):
        s1 = StarSystem("Solar", "Yellow dwarf", "Single",
                        5, (2, 4))

        s2 = StarSystem("Sigma", "Red dwarf", "Single",
                        5, (3, 5))

        self.assertEqual(StarSystem.compare_star_systems(s1, s2),
                         f"{s2.name} has a wider or equal habitable zone compared to {s1.name}.")

if __name__ == '__main__':
    unittest.main()