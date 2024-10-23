"""
Advent of code 2023 day 2 solution (written in Python)
    by stafford-m
"""
import re

d2_file = open("./inputs/input_d2.txt")
part_one_sum = 0
part_two_sum = 0
cube_max = {
    "red"   : 12,
    "green" : 13,
    "blue"  : 14
}
# -----------------------------------------------------------------

def part_one(line_in):
    # getting game number, then putting all cube drawns into a list of tuples
    # any draw that violates maximum results in 0 return
    game_number = int(re.match(r"Game (\d+):", line_in).group(1))
    cubes_drawn = re.findall(r"(\d+) (red|green|blue)", line_in)
    for cube_set in cubes_drawn:
        if cube_max[cube_set[1]] < int(cube_set[0]):
            return 0
    return game_number

def part_two(line_in):
    minimum_cubes = {
        "red"   : 0,
        "green" : 0,
        "blue"  : 0
    }
    # each color is put into it's own tuple in a list
    # each tuple is then used to compare and find the highest required number for any given cube color
    # type-casting was needed for comparisons and addition
    cubes_drawn = re.findall(r"(\d+) (red|green|blue)", line_in)
    for cube_set in cubes_drawn: 
        if int(cube_set[0]) > minimum_cubes[cube_set[1]]:
            minimum_cubes[cube_set[1]] = int(cube_set[0])
    
    return minimum_cubes["red"] * minimum_cubes["green"] * minimum_cubes["blue"]
    
# -----------------------------------------------------------------

for line in d2_file:
    part_one_sum += part_one(line)
    part_two_sum += part_two(line)

print(f"Part one solution: {part_one_sum}")
print(f"Part two solution: {part_two_sum}")
d2_file.close()