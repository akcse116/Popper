import unittest
import JSMethods

class TestJSMethods(unittest.TestCase):
    def test_saveJson(self):

        test = {'time': 12345678, "player001": {'angle': 105, 'score': 50000}}
        compare = '{"time": 12345678, "player001": {"angle": 105, "score": 50000}}'

        self.assertTrue(JSMethods.toJson(test) == compare, "dumps Returned: " + JSMethods.toJson(test) + " needed: " + compare)


    def test_loadJson(self):

        test = '{"time": 12345678, "player001": {"angle": 105, "score": 50000}}'
        compare = {'time': 12345678, "player001": {'angle': 105, 'score': 50000}}

        self.assertTrue(JSMethods.fromJson(test) == compare, JSMethods.fromJson(test))


    def test_saveLoad(self):

        filename = "testFile.jsom"
        test = '{"time": 12345678, "player001": {"angle": 105, "score": 50000}}'

        JSMethods.saveGameState(test, filename)

        self.assertTrue(JSMethods.getGameState(filename) == test, JSMethods.getGameState(filename))


if __name__ == '__main__':
    unittest.main()
