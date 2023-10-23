def is_construction_possible(word, words_set, is_original=True) -> bool:
    """
        - param: `word` The current word under verification
        - param: `words_set` the set of words from the input file
        - param: `is_original` A flag indicating whether the current word is the original or new constructed one

        Returns: bool - `True` if the word can be constructed otherwise `False`.
    """

    # check if the `word` is already in `words_set`
    # if so, then verify that the word is NOT the original word.
    if word in words_set and not is_original:
        return True  # shows that the word can be constructed.

    # here now check for each index of the `word` start from index 1 to last index of the word
    # get a prefix
    # get corresponding suffix
    for i in range(1, len(word)):
        prefix = word[:i]
        suffix = word[i:]

        # check if the prefix is not in words_set and if the prefix is in words_set means we have got the first word
        # now recursively check if the suffix can further be constructed and set the `is_original` = False
        if prefix in words_set and is_construction_possible(suffix, words_set, is_original=False):
            return True  # shows that the word can be constructed.

    return False


def find_longest_compound_words(file_path: str) -> tuple:
    # Read the file to get the list of words.
    with open(file_path, 'r') as file:
        words = [line.strip() for line in file.readlines()]
    
    # Convert `list` to `set` for O(1) time complexity look-ups
    words_set = set(words)

    # Sort words by length (from longest to shortest)
    words.sort(key=len, reverse=True)  # TrimSort algorithm (merge sort + insertion sort)

    # initialize both the variables to be None.
    longest_word, second_longest_word = None, None

    # loop through the list of sorted words (longest to smallest)
    for word in words:

        # if the construction is possible for the current word.
        if is_construction_possible(word, words_set):
            if longest_word is None:
                longest_word = word  # first constructed word is be the longest word
            elif second_longest_word is None:
                second_longest_word = word  # second constructed word is be the second-longest word

                # once the second-largest word is encountered, that is the end of the looping
                # as the list if already sorted.
                break

    # Since the words list is sorted from (longest to smallest)
    # - the first possible constructed word will be the `longest_word`
    # - the second possible constructed word will be the `second_largest_word`
    return longest_word, second_longest_word


if __name__ == "__main__":
    import time

    # Test for Input_01.txt
    start_time = time.time()
    longest, second_longest = find_longest_compound_words("Input_01.txt")
    print(f"Input_01.txt Results:")
    print(f"1. Longest Compound Word: {longest}")
    print(f"2. Second Longest Compound Word: {second_longest}")
    print(f"Time taken: {time.time() - start_time:.4f} seconds\n")

    # Test for Input_02.txt
    start_time = time.time()
    longest, second_longest = find_longest_compound_words("Input_02.txt")
    print(f"Input_02.txt Results:")
    print(f"1. Longest Compound Word: {longest}")
    print(f"2. Second Longest Compound Word: {second_longest}")
    print(f"Time taken: {time.time() - start_time:.4f} seconds")

    # NOTE: Input_01.txt and Input_02.txt should be in the same directory as the `solution.py`
