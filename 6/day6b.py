import collections
import itertools


CONDITION = 14

with open('input.txt') as t:
    message = collections.deque(t.read())

for i in range(0,len(message)):
    if len(set(itertools.islice(message, 0, CONDITION))) == CONDITION:
        print(i+CONDITION)
        break
    else:
        message.popleft()
            
