#! /usr/bin/env python
# Do not modify this file.  It is used by the autograder.

import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os 

script_name = sys.argv[0] 
base_name = os.path.basename(script_name)
lab_name = os.path.splitext(base_name)[0].split("_")[-1]
lab_dir = '../src/' + lab_name

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), lab_dir)))
from main import main

class TestLargestAndSmallest(unittest.TestCase):
    def test_main(self):
        test_cases = [
            {'input': '5\n10\n-3\n8\n2\n', 'output': '10\n-3\n'},
            {'input': '1\n1\n1\n1\n1\n', 'output': '1\n1\n'},
            {'input': '-5\n-2\n-3\n-1\n-4\n', 'output': '-1\n-5\n'},
            {'input': '0\n1\n2\n3\n4\n', 'output': '4\n0\n'},
            {'input': '10\n9\n8\n7\n6\n', 'output': '10\n6\n'},
            {'input': '1\n2\n3\n4\n0\n', 'output': '4\n0\n'},
            {'input': '4\n3\n2\n1\n0\n', 'output': '4\n0\n'},
            {'input': '-1\n-2\n-3\n-4\n-5\n', 'output': '-1\n-5\n'},
            {'input': '-1\n-1\n-1\n-1\n-1\n', 'output': '-1\n-1\n'},
            {'input': '1\n2\n3\n2\n1\n', 'output': '3\n1\n'}
        ]
        for i, test_case in enumerate(test_cases):
            with patch('sys.stdin', StringIO(test_case['input'])):
                with patch('sys.stdout', new=StringIO()) as fake_output:
                    main()
                    expected_output = test_case['output']
                    self.assertEqual(fake_output.getvalue(), expected_output, f'Test case {i+1} failed')

if __name__ == '__main__':
    unittest.main()