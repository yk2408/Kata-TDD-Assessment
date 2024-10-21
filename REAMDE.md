# TDD-Assessment: String Calculator
This repository contains a simple String Calculator implemented in Python and tests is written using unittests. The calculator is designed to add numbers represented in a specific string format, adhering to Test-Driven Development (TDD) principles. Each feature has corresponding test cases to ensure correct functionality and edge-case handling.

### Table of Contents
1. Features
2. Installation
3. Usage
4. Test Cases
5. Scenarios

### Features
1. Addition of Numbers: Supports addition of numbers in a comma-separated string format.
2. New Line Support: Handles new line characters as additional delimiters between numbers.
3. Custom Delimiters: Users can define custom delimiters by specifying them in a specific format.
4. Negative Number Handling: Throws an exception when negative numbers are encountered, listing all negatives in the error message.
5. Ignoring Large Numbers: Numbers greater than 1000 are excluded from the summation.
6. Multi-Character Delimiters: Allows delimiters of any length and supports multiple delimiters within a single string.

### Installation
To use this String Calculator, ensure you have Python installed on your machine. Clone the repository and navigate to the project directory. Run the test cases using:
```commandline
python -m unittest test_string_calculator.py
```

### Usage
The main functionality is provided by the add() function, which takes a string as input and returns the sum of numbers based on the supported formats and rules.

### Test Cases
The project follows a TDD approach with the following key test cases covered in test_string_calculator.py:

1. Empty String: `add("")` returns 0.
2. Single Number: `add("100")` returns 100.
3. Multiple Numbers: Handles addition of any number of numbers. 
4. New Line Support: Handles new lines between numbers `add("11\n12,13")` returns 36. 
5. Custom Delimiter Support: Supports custom delimiters specified in the input string e.g., `add("//;\n1;2")` returns 3. 
6. Negative Number Exception: Raises an exception for negative numbers e.g., `add("1,-2,-3")` throws an error listing the negative numbers: `"-2,-3"`. 
7. Ignoring Large Numbers: Ignores numbers greater than 1000 during summation e.g., `add("2,2001")` returns 2. 
8. Multi-Character Delimiters: Supports delimiters of any length, e.g., `add("//[***]\n10***20***30")` returns 60.
9. Multiple Delimiters: Handles multiple delimiters, e.g., `add("//[*][%]\n1*2%3")` returns 6.