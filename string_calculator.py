import re


class StringCalculator:
    def __init__(self, numbers: str):
        self.numbers = numbers

    def get_delimiters(self) -> str:
        """
        Extract delimiters from the given string
        :return: delimiter string
        """
        # Check if custom delimiter is present
        if self.numbers.startswith('//'):
            # Split into delimiter and numbers
            delimiter_part, numbers_part = self.numbers.split('\n', 1)

            # Extract delimiters, supporting multiple delimiters of any length
            custom_delimiters = re.findall(r'\[(.*?)\]', delimiter_part)

            if not custom_delimiters:
                custom_delimiter = delimiter_part[2:]  # Fallback for a single character
                custom_delimiters = [custom_delimiter]

            # Join delimiters and add escape character to avoid matching regex issue
            delimiter = '|'.join(map(re.escape, custom_delimiters))
            self.numbers = numbers_part  # The rest of the numbers remain unchanged
        else:
            # Default delimiter is a comma
            delimiter = ','
        return delimiter

    def add(self) -> int:
        """
        Adds all given numbers
        :return: total of given numbers
        """
        if not self.numbers:
            return 0

        delimiter = self.get_delimiters()

        # Replace newline with comma
        self.numbers = self.numbers.replace('\n', ',')

        # Split the string using regex for multiple delimiters
        nums_list = [int(num) for num in re.split(delimiter, self.numbers) if num]

        # raise value error for negative numbers
        negative_nums = ', '.join([str(num) for num in nums_list if num < 0])
        if negative_nums:
            raise ValueError(f"negative numbers not allowed: {negative_nums}")

        return sum(nums_list)


if __name__ == '__main__':
    numbers_list = ["1\n2,3", "//;\n1;2", "//[***]\n1***2***3", "//[*][%]\n1*2%3", "-11,2,-100"]
    for numbers in numbers_list:
        print(StringCalculator(numbers).add())
