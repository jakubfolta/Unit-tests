import unittest
from fullNames import getFullName

class NamesTestCase(unittest.TestCase):

    def test_firstLast(self):
        fullName = getFullName('janis', ' joplin')
        self.assertEqual(fullName, 'Janis Joplin')

unittest.main()
