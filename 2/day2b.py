def value(pair):
    match pair:
        case 'A Z' | 'B Y' | 'C X': return 2
        case 'A Y' | 'B X' | 'C Z': return 1
        case _: return 3

def result(shape):
    match shape:
        case 'X': return 0
        case 'Y': return 3
        case 'Z': return 6

with open('input.txt') as t:
    m = [value(x.strip())+ result(x.strip()[-1]) for x in t.readlines()]

print(sum(m))

