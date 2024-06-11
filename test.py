import unittest
import blah

class TestBlah(unittest.TestCase):
    def test_blah_1(self):
        """
        Test that it can sum a list of integers
        """
        bottle_lvl = blah.Bottle_Level()
        bottle_lvl.bottles = [['b','y','b','y'], ['y','b','y','b'], []]
        bottle_lvl.max_depth = 4
        res = bottle_lvl.solve()
        self.assertEqual(True, res[0])

    def test_blah_2(self):
        """
        Test that it can sum a list of integers
        """
        bottle_lvl = blah.Bottle_Level()
        bottle_lvl.bottles = [['y','y','b','b'], ['b','r','y','y'], ['r','r','r','b'], [], []]
        bottle_lvl.max_depth = 4
        res = bottle_lvl.solve()
        self.assertEqual(True, res[0])

    def test_blah_3(self):
        """
        Test that it can sum a list of integers
        """
        bottle_lvl = blah.Bottle_Level()
        bottle_lvl.bottles = [['r','y','r','y'], ['b','r','y','b'], ['r','y','b','b'], [], []]
        bottle_lvl.max_depth = 4
        res = bottle_lvl.solve()
        self.assertEqual(True, res[0])
        
    def test_blah_4(self):
        """
        Test that it can sum a list of integers
        """
        bottle_lvl = blah.Bottle_Level()
        bottle_lvl.bottles = [['r','y','r','y'], ['b','r','y','b'], ['r','y','b','b'], [], []]
        bottle_lvl.max_depth = 4
        res = bottle_lvl.solve()
        self.assertEqual(True, res[0])

if __name__ == '__main__':
    unittest.main()

