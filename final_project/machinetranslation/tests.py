import unittest

from translator import englishToFrench, frenchToEnglish

class Test_englishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench(""), "") # test when 2 is given as input the output is 4.
        self.assertEqual(englishToFrench("Hello"), "Bonjour")  # test when 3.0 is given as input the output is 9.0.
       
class Test_frenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish(""), "") # test when 2 is given as input the output is 4.
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")  # test when 3.0 is given as input the output is 9.0.



unittest.main()
