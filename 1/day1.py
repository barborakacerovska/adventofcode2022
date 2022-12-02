import csv

with open('inputdata.csv', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
 
    space = 1
    calories_list = []
    elves_total_calories = {}

    for row in csv_reader:
        if row != []:
            elves = {}
            calories_list.append(int(row[0]))
            elves.update({'elf_order': space, 'calories_list': calories_list})
        else:
            elves_total_calories.update({space: sum(calories_list)})
            calories_list = []
            space += 1

print('Maximum calories: ', max(elves_total_calories.values()))

# 2nd part

elves_sorted = (dict(sorted(elves_total_calories.items(), key=lambda item: item[1],reverse = True)))
elves_top_3 = dict(list(elves_sorted.items())[0:3])
print('Top 3 calories - total:', sum(elves_top_3.values()))


