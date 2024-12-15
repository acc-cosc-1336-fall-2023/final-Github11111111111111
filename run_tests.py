#DON'T MAKE CHANGES TO THIS FILE

#write tests for all the questions here

import unittest

from tests.question_tests import question_tests

suite = unittest.TestLoader().loadTestsFromModule(question_tests)
unittest.TextTestRunner(verbosity=2).run(suite)

def test_get_most_likely_ancestor_consensus():
    """
    Test function for get_most_likely_ancestor_consensus.
    """
    dna_string1 = "GATATATGCATATACTT"
    dna_string2 = "ATAT"

    positions = get_most_likely_ancestor_consensus(dna_string1, dna_string2)

    pos1, pos2, pos3 = positions

    print(f"Test case result: {pos1}, {pos2}, {pos3}")

if __name__ == "__main__":
    main()
    test_get_most_likely_ancestor_consensus()