"""

Advent of code 2023 solution
    by stafford-m
    
- the "numbers" dictionary is like that because the act of replacing the values in the 
    string is sometimes destructive to other values in the string:
    eightwothree could come out to two different values based on whether your implementation
    seeks to replace eights or twos first. The correct version would be both (823).

"""
d1_file = open("./inputs/input_d1.txt", "r")
part_one_sum = 0
part_two_sum = 0
numbers = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
    "zero": "z0o"
}

def part_one(file_string):
    
    l_digits = [i for i in file_string if i.isdigit()]
    return int(l_digits[0] + l_digits[-1])

def part_two(file_string):
    
    for i in numbers:
        file_string = file_string.replace(i, numbers[i])
        
    return part_one(file_string)
    
# -------------------------------------------------------------------

for line in d1_file:
    part_one_sum += part_one(line)
    part_two_sum += part_two(line)
    
print(f"Day one, part one solution: {part_one_sum}")
print(f"Day one, part two solution: {part_two_sum}")

d1_file.close()