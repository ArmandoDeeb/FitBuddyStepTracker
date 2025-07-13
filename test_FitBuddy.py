import unittest
from unittest.mock import mock_open, patch
from io import StringIO

class TestFitBuddyFunctions(unittest.TestCase):
    def test_summary_calculates_correct_total_and_average(self):
        # Testcase 1 -  checks show all function with default file values
        fake_data = (
            "2025-06-01,4567\n"
            "2025-06-02,6290\n"
            "2025-06-03,7100\n"
            "2025-06-04,7500\n"
            "2025-06-05,9120\n"
        )
        # patches the open call and the global 'file' in FitBuddy
        with patch("builtins.open", mock_open(read_data=fake_data)):
            import FitBuddy
            FitBuddy.file = open("test_log.txt","r")

            with patch("sys.stdout", new=StringIO()) as fake_out:
                FitBuddy.Summary()
                output = fake_out.getvalue()
        
        self.assertIn("Total steps: 34577", output)
        self.assertIn("Average steps: 6915.4", output)

if __name__ == "__main__":
    unittest.main()