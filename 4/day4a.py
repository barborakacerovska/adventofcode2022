
def get_ordered(pair):
    """
    order by the first number, or second if the first numbers are equal
    """
    if get_number(pair,0,0) > get_number(pair,1,0):
        return pair[::-1]
    if (get_number(pair,0,0) ==  get_number(pair,1,0)) and (get_number(pair,0,1) <  get_number(pair,1,1)):
        return pair[::-1]
    else:
        return pair

def get_number(pair,a,b):
    return int(pair[a].split('-')[b])

def compare_last(pair):
    """
    compare the last numbers of the pair
    """
    if int(pair[0].split('-')[1]) >= int(pair[1].split('-')[1]):
        return 1
    else:
        return 0

with open('input.txt') as t:
   common_values = ([compare_last(get_ordered(x.strip().split(','))) for x in t.readlines()])
    

print(sum(common_values))