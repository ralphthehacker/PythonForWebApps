import re

#Creating a variable to count all numbers
number_counter = 0
regex_pattern = "[0-9]+" #And a pattern to use for the regex logic

#Opening the text data. This path corresponds to my folder's path
with open("/Users/ralphblanes/PycharmProjects/PythonForWebApps/sample.txt") as data_file:
    for line in data_file.readlines():
        #Finding the numbers in every line
        numbers = re.findall(regex_pattern,line)
        sum_numbers = sum([int(x) for x in numbers]) #And summing them after casting them to integers
        number_counter += sum_numbers
#Then, print the total sum after processing the entire file
print(number_counter)