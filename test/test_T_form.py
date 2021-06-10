import unittest
import myform

class Test_T_Form(unittest.TestCase):
    def test_A(self):
        list_mail_cor = ["dsdak@mail.ru", "sads@yandex.ru", "ipjb@gmail.com", "asd@rosphoto.org"]
        list_quest_cor = ["Hello", "I have a question"]
        i = 0
        k = 0
        while i < len(list_mail_cor):
            while k < len(list_quest_cor):
                self.assertTrue(myform.my_formTest(list_mail_cor[i], list_quest_cor[k]))
                k += 1
            i += 1

if __name__ == '__main__':
    unittest.main()
