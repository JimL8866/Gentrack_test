import unittest
from solution import app


class TestClass(unittest.TestCase):
    def test_create_csv(self):
        self.assertEqual(app.create_csv("testing_case_1.xml"), False, "Test Data row 200, 300 must within header and trailer rows")
        self.assertEqual(app.create_csv("testing_case_2.xml"), False, "Test Data has header more than one")
        self.assertEqual(app.create_csv("testing_case_3.xml"), False, "Test Data has trailer more than one")
        self.assertEqual(app.create_csv("testing_case_4.xml"), False, "Test Data doesn't have 200 row")
        self.assertEqual(app.create_csv("testing_case_5.xml"), False, "Test Data doesn't have 300 row")
        self.assertEqual(app.create_csv("testing_case_6.xml"), False, "Test Data row 200, 300 must within header and trailer rows")
        self.assertEqual(app.create_csv("testing_case_7.xml"), False, "Test Data doesn't have 100 row")
        self.assertEqual(app.create_csv("testing_case_8.xml"), False, "Test Data doesn't have 900 row")
        self.assertEqual(app.create_csv("testing_case_9.xml"), False, "Test Data row 200, 300 must within header and trailer rows")
        self.assertEqual(app.create_csv("testing_case_10.xml"), False, "Test Data row 200 doesn't followed by at least one 300row")
        self.assertEqual(app.create_csv("testfile.xml"), "CSV files generated successfully!","Test Data valid")
if __name__ == "__main__":
    unittest.main()
