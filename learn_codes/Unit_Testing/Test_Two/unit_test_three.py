from learn_codes.Unit_Testing.Test_Two.Employee import Empl
import unittest


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("-------- It Runs Before The Test Starts ---------\n\n")

    def setUp(self) -> None: # Runs Before Each Test
        self.emp1 = Empl("Krishna", "Singh", 1500000)
        self.emp2 = Empl("Hari", "Om", 16849165198)
        print('********* Set Up **********')

    def tearDown(self) -> None:
        print('********* Tear Down ********\n')

    @classmethod
    def tearDownClass(cls) -> None:
        print("--------- It Runs After The Test Finishes ---------\n")

    def test_email(self):

        print('Test Email Runs')

        # emp1 = Empl("Krishna", "Singh", 1500000)
        # emp2 = Empl("Hari", "Om", 16849165198)

        self.assertEqual(self.emp1.email, "Krishna.Singh@gmail.com")
        self.assertEqual(self.emp2.email, "Hari.Om@gmail.com")

        self.emp1.first = "KrishnaChange"
        self.emp2.first = "HariChange"

        self.assertEqual(self.emp1.email, "KrishnaChange.Singh@gmail.com")
        self.assertEqual(self.emp2.email, "HariChange.Om@gmail.com")

    def test_fullname(self):

        print('Test Fullname Runs')

        # emp1 = Empl("Krishna", "Singh", 1500000)
        # emp2 = Empl("Hari", "Om", 16849165198)

        self.assertEqual(self.emp1.fullname, "Krishna Singh")
        self.assertEqual(self.emp2.fullname, "Hari Om")

if __name__ == "__main__":
    unittest.main()