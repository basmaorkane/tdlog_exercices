"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""

"""
Create unit test using those cases:
fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)
"""
import unittest
def solution(string, ending):
    return string.endswith(ending)


class TestSolution(unittest.TestCase):
    
    def test_fixed_tests_true(self):
        fixed_tests_True = (
            ("samurai", "ai"),
            ("ninja",   "ja"),
            ("sensei",  "i"),
            ("abc",     "abc"),
            ("abcabc",  "bc"),
            ("fails",   "ails"),
        )
        for s, e in fixed_tests_True:
            with self.subTest(s=s, e=e):
                self.assertTrue(solution(s, e))
    
    def test_fixed_tests_false(self):
        fixed_tests_False = (
            ("sumo",    "omo"),
            ("samurai", "ra"),
            ("abc",     "abcd"),
            ("ails",    "fails"),
            ("this",    "fails"),
            ("spam",    "eggs"),
        )
        for s, e in fixed_tests_False:
            with self.subTest(s=s, e=e):
                self.assertFalse(solution(s, e))

# Pour exécuter les tests
if __name__ == "__main__":
    unittest.main()
