import unittest

from mullawatch import models, reports

class ReportsTest(unittest.TestCase):
    def test_generate_report(self):

        transaction1 = models.Transaction(account_id=1, category_id=1, amount=258, date='2023-11-04')
        transaction2 = models.Transaction(account_id=2, category_id=2, amount=-128, date='2023-11-06')

        report = reports.generate_report('2023-11-04', '2023-11-06')

        self.assertEqual(report['income'], 258)
        self.assertEqual(report['expenses'], 128)

if __name__ == '__main__':
    unittest.main()