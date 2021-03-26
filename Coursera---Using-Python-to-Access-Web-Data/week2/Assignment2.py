import re

name = input('Enter the name of the file: ')
if len(name) < 1: name = 'regex_sum_1131095.txt'

handle = open(name)

smallNums = 0
for line in handle:
    # print(line)
    numbers = re.findall(r'\d+', line)
    if len(numbers) == 0: continue
    for num in numbers:
        smallNums += int(num)

print(f'i\'m the sum {smallNums} ')



