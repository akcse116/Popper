import unittest
import server


class TestServer(unittest.TestCase):

    def test_index(self):
        file = ""
        with open("index.html") as doc:
            for line in doc:
                line = line.rstrip('\r\n')
                file += line

        # self.assertTrue(server.index() == file, "index mis-match")


if __name__ == '__main__':
    unittest.main()
