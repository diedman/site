import unittest
import myform

class Test_test_1(unittest.TestCase):
    def test_A(self):
        list_mail_cor = ["sdfjhyandex.ru", "klasjfh@gmailcom", "sadj@mail.u"]
        i = 0
        while i < len(list_mail_cor):
            self.assertFalse(myform.patternTest(list_mail_cor[i]))
            i += 1

if __name__ == '__main__':
    unittest.main()
