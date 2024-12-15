#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    import unittest
from dna_substring_positions import get_most_likely_ancestor_consensus

class TestGetMostLikelyAncestorConsensus(unittest.TestCase):

    def test_multiple_occurrences(self):
        # Parameters
        dna_string1 = "GATATATGCATATACTT"
        dna_string2 = "ATAT"

        # Expected result
        expected_positions = (2, 4, 10)

        # Call the function
        result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)

        # Save each value to a variable
        pos1, pos2, pos3 = result

        # Assertions
        self.assertEqual(result, expected_positions)
        self.assertEqual(pos1, 2)
        self.assertEqual(pos2, 4)
        self.assertEqual(pos3, 10)

if __name__ == "__main__":
    
 




