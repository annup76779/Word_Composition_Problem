# Compound Word Finder
The longest and second-longest compound words are determined by this programme from a list of words. When two shorter words from the same file are combined (concatenated), the result is a compound word.

## Overview
The key to the approach is the effective application of data structures to swiftly ascertain whether a word can be formed from other words in the list. Performance is given top priority by the programme, ensuring quick results even for lists with more than 100,000 entries.

## Design Decisions & Approach:
1. Data Structures:

    - Used a list and a set to store words. While the set enables quick O(1) lookups to quickly confirm a word's existence, the list enables processing based on word length.
2. Recursive Decomposition:

    - The core logic is based on recursively checking if a word can be broken down into smaller constituent words from the list. This ensures a systematic and comprehensive approach to detect compounded words.
3. Performance Optimizations:

    - To ensure timely results even for very large lists, words are processed in descending order of their length. This allows the program to identify the longest compounded words early in the search process, minimizing redundant checks.
## Steps to Execute:

1. Ensure you have Python 3.x installed.
2. Place your input word list files in the same directory as the script. Name them appropriately - `Input_01.txt`, `Input_02.txt`.
3. Open terminal and navigate to the directory where you have placed all the `Input files` and `solution.py`.
4. Run the script: 
```python solution.py```

1. Results (longest and second-longest compounded words, and processing time) will be displayed in the console.
