def result(pair):
    match pair:
        case 'A Y' | 'B Z' | 'C X': return 6
        case 'A X' | 'B Y' | 'C Z': return 3
        case _: return 0

def value(shape):
    match shape:
        case 'X': return 1
        case 'Y': return 2
        case 'Z': return 3

with open('input.txt') as t:
    m = [result(x.strip())+ value(x.strip()[-1]) for x in t.readlines()]

print(sum(m))

