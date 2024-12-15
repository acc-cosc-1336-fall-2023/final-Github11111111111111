def find_substring_locations(dna_string1, dna_string2):
    """
    This function finds all locations of dna_string2 as a substring of dna_string1.

    Parameters:
    dna_string1 (str): The main DNA string.
    dna_string2 (str): The substring DNA string to find in dna_string1.

    Returns:
    list: A list of starting positions (1-based index) where dna_string2 is found in dna_string1.
    """
    locations = []
    
    for i in range(len(dna_string1) - len(dna_string2) + 1):
        if dna_string1[i:i+len(dna_string2)] == dna_string2:
            locations.append(i + 1)

    return locations

def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    """
    This function finds the starting positions of dna_string2 in dna_string1
    and returns them as multiple parameters.

    Parameters:
    dna_string1 (str): The main DNA string.
    dna_string2 (str): The substring DNA string to find in dna_string1.

    Returns:
    Multiple integers: Starting positions (1-based index) of dna_string2 in dna_string1.
    """
    locations = find_substring_locations(dna_string1, dna_string2)
    return tuple(locations)