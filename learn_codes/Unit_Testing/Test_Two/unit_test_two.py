from learn_codes.Unit_Testing.Test_Two.Employee import Empl
import unittest


class TestEmployee(unittest.TestCase):

    def test_email(self):

        emp1 = Empl("Krishna", "Singh", 1500000)
        emp2 = Empl("Hari", "Om", 16849165198)

        self.assertEqual(emp1.email, "Krishna.Singh@gmail.com")
        self.assertEqual(emp2.email, "Hari.Om@gmail.com")

        emp1.first = "KrishnaChange"
        emp2.first = "HariChange"

        self.assertEqual(emp1.email, "KrishnaChange.Singh@gmail.com")
        self.assertEqual(emp2.email, "HariChange.Om@gmail.com")

    def test_fullname(self):

        emp1 = Empl("Krishna", "Singh", 1500000)
        emp2 = Empl("Hari", "Om", 16849165198)

        self.assertEqual(emp1.fullname, "Krishna Singh")
        self.assertEqual(emp2.fullname, "Hari Om")

