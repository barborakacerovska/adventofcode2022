import re
import numpy as np

def get_stack(stack):
    # create empty list in corresponding shape
    stack_new = [['0' for x in range(len(stack))] for y in range(len(stack[0]))]
    # 'reshape' lists
    for i, row in enumerate(stack):
        for j, letter in enumerate(row):
            stack_new[j][len(stack)-1-i] = letter
    return stack_new

def remove_words(move):
    # removes 'move ', replaces ' from ' and ' to ' with comma 
    return re.sub('move ', '', re.sub(' from ', ',', re.sub(' to ', ',', move)))

def move_crate(move, stack):
    stack_new = stack.copy()
    stack_from = stack_new[move[1]]
    stack_to = stack_new[move[2]]
    position_from = get_last_crate_position(stack_from)
    for i in range(move[0], 0, -1):
        letter = stack_from[position_from-i]
        stack_from[position_from-i] = ' '
        position_to = get_last_crate_position(stack_to)
        if position_to == len(stack_to):
            stack_to.append(letter)
        else:
            stack_to[position_to] = letter
    return stack_new

def get_last_crate_position(position):
    try:
        last_pos = position.index(' ')
    except ValueError:
        last_pos = len(position) 
    return last_pos

def print_last_position(stack):
    for i in stack_dict.values():
        try: 
            print(i[get_last_crate_position(i)-1], end ="")
        except KeyError:
            print(i[-1], end ="")


with open('input3.txt') as t:
    stack_input, moves_input = [a for a in t.read().split("\n\n")]

# transposes list
stack = get_stack([[y.replace("[", " ").replace("]", " ") for y in x] for x in stack_input.split("\n")])
# filters empty rows
stack = [i for i in stack.copy() if i[0] != ' ']
# stack to dict 
stack_dict = {key+1:value for (key,value) in enumerate(stack)}

# cleans moves
moves = [[int(j) for j in remove_words(i).split(',')] for i in moves_input.split("\n")]

# move crates
for move in moves:
    move_crate(move, stack_dict)

# print last crate
print_last_position(stack_dict)



