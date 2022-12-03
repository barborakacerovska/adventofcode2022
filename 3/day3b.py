
import string

def get_common(group):
    return list(set(group[0]).intersection(set(group[1])).intersection(set(group[2])))[0]

def get_groups(text):
    groups = []
    lines_iter = iter(text.splitlines())  
    for lines in zip(lines_iter, lines_iter, lines_iter):
        groups.append(lines)
    return groups


alphabet = list(string.ascii_letters)

with open('input.txt') as t:
    groups = get_groups(t.read())
    priorities = [alphabet.index(get_common(group))+1 for group in groups]

print("The sum of the priorities is", sum(priorities))
