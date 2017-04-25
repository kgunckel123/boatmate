import unittest
from model import schedule_optimize
from helper_functions import make_weights_from_input_dict


class TestModel(unittest.TestCase):

    def test_base_case(self):
        weights=[10, 10, 10, 10, 14, 14, 5, 5, 6, 6, 6, 6, 5, 5, 5, 1, 1, 1, 1, 11, 11, 11, 9, 9, 13, 13, 13]
        length=len(weights)
        print(length)
        val = schedule_optimize(weights)
        expected = {}  # put expected here
        self.assertEqual(val, expected)

    def test_make_weights(self):
        bases = {'Duck Boat': 5,
                 'Pontoon': 4}

        components = {'Pinstripe': 5,
                      'Runway': 5,
                      'Both': 9,
                      'Neither': 0}
        input_dic = {('Duck Boat', 'Pinstripe'): 3,
                    ('Pontoon', 'Both'):4}
        output_weights, output_types=make_weights_from_input_dict(input_dic, bases, components)
        expected_weights=[10, 10, 10, 13, 13, 13, 13]
        expected_output_types=['Duck Boat Pinstripe','Duck Boat Pinstripe','Duck Boat Pinstripe',
                               'Pontoon Both','Pontoon Both','Pontoon Both','Pontoon Both']
        self.assertEqual(output_weights,expected_weights)
        self.assertEqual(output_types, expected_output_types)

class TestGUI(unittest.TestCase):

    def test_functions(self):
        pass


if __name__ == "__main__":
    unittest.main()