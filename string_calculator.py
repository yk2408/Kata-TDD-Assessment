import re


class StringCalculator:
    @staticmethod
    def get_delimiters(numbers: str) -> tuple:
        """
        Extract delimiters from the given string
        :param: numbers:
        :return: delimiter string
        """
        # Check if custom delimiter is present
        if numbers.startswith('//'):
            # Split into delimiter and numbers
            delimiter_part, numbers_part = numbers.split('\n', 1)

            # Extract delimiters, supporting multiple delimiters of any length
            custom_delimiters = re.findall(r'\[(.*?)\]', delimiter_part)

            if not custom_delimiters:
                custom_delimiter = delimiter_part[2:]  # Fallback for a single character
                custom_delimiters = [custom_delimiter]

            # Join delimiters and add escape character to avoid matching regex issue
            delimiter = '|'.join(map(re.escape, custom_delimiters))
            numbers = numbers_part  # The rest of the numbers remain unchanged
        else:
            # Default delimiter is a comma
            delimiter = ','
        return delimiter, numbers

    def add(self, numbers: str) -> int:
        """
        Adds all given numbers
        :param: numbers:
        :return: total of given numbers
        """
        if not numbers:
            return 0

        delimiter, cleaned_numbers = self.get_delimiters(numbers)

        # Replace newline with comma
        cleaned_numbers = cleaned_numbers.replace('\n', ',')

        # Split the string using regex for multiple delimiters
        nums_list = [int(num) for num in re.split(delimiter, cleaned_numbers) if num]

        # raise value error for negative numbers
        negative_nums = ', '.join([str(num) for num in nums_list if num < 0])
        if negative_nums:
            raise ValueError(f"negative numbers not allowed: {negative_nums}")

        # skip numbers greater than 1000
        nums_list = [num for num in nums_list if num <= 1000]

        return sum(nums_list)


if __name__ == '__main__':
    numbers_list = ["1\n2,3", "//;\n1;2", "//[***]\n1***2***3", "//[*][%]\n1*2%3", "1001,2", "-11,2,-100"]
    for numbers in numbers_list:
        print(StringCalculator().add(numbers))
