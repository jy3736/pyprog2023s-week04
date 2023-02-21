# Do not modify this file.  It is used by the autograder.

# Do not modify this file.  It is used by the autograder.

import unittest
from io import StringIO
from unittest.mock import patch
import sys, os

script_name = sys.argv[0]
base_name = os.path.basename(script_name)
lab_name = os.path.splitext(base_name)[0].split("_")[-1]
lab_dir = '../src/' + lab_name

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), lab_dir)))
from main import main

class TestMain(unittest.TestCase):
    def test_main(self):
        test_cases = [
            {'input': '1 2 3 4 5\n', 'output': '3 2\n'},
            {'input': '2 3 4 5 1\n', 'output': '3 1\n'},
            {'input': '1 2 4 5 3\n', 'output': '3 4\n'},
            {'input': '3 4 5 1 2\n', 'output': '3 0\n'},
            {'input': '5 4 1 3 2\n', 'output': '3 3\n'},
        ]
        for i, test_case in enumerate(test_cases):
            print(f"{test_case['input']}{test_case['output']}")
            with patch('sys.stdin', StringIO(test_case['input'])):
                with patch('sys.stdout', new_callable=StringIO) as fake_out:
                    main()
                    self.assertEqual(fake_out.getvalue(), test_case['output'], f'Test case {i} failed')

if __name__ == '__main__':
    unittest.main()
