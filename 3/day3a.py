
import string


def get_halves(x):
    string1 = x[0:len(x)//2]
    string2 = x[len(x)//2: len(x)]
    return (string1, string2)

def get_common(pair):
    # itersection of two sets converted to a list
    return list(set(pair[0]).intersection(set(pair[1])))[0]

alphabet = list(string.ascii_letters)

with open('input.txt') as t:
    """ 
    1.split into halves
    2.get the common letter
    3.get the lettter order in the alphabet by getting index + 1
    """
    priorities = [alphabet.index(get_common(get_halves(x.strip())))+1 for x in t.readlines()]

    
print("The sum of the priorities is", sum(priorities))