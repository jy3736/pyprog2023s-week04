# Do not modify this file.  It is used by the autograder.

import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os 
import random

script_name = sys.argv[0] 
base_name = os.path.basename(script_name)
lab_name = os.path.splitext(base_name)[0].split("_")[-1]
lab_dir = '../src/' + lab_name

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), lab_dir)))
from main import main

class TestSorting(unittest.TestCase):
    
    def test_sorting(self):
        for i in range(5):
            a, b, c, d = random.sample(range(101), 4)
            input_str = f"{a} {b} {c} {d}\n"
            sorted_str = " ".join(map(str, sorted([a, b, c, d])))
            expected_output = sorted_str + "\n"
            print(f"{input_str}{expected_output}")
            with self.subTest(input=input_str, output=expected_output):
                with unittest.mock.patch('builtins.input', return_value=input_str):
                    with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                        main()
                        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()