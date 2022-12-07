import string

rucksacks = open("day3/input.txt")

letters = [a for a in string.ascii_lowercase] + [A for A in string.ascii_uppercase]
priorities = {let: num+1 for num, let in enumerate(letters)}

prioritems = []
badges = []
badcol = []
for line in rucksacks:
  line = line.strip()
  badcol.append(line)
  if len(badcol) == 3:
    bshared = [i for i in badcol[0] if i in badcol[1] and i in badcol[2]][0]
    badges.append(priorities[bshared])
    badcol = []
  size = int(len(line)/2)
  comp1 = line[0:size]
  comp2 = line[size:]
  shared = [i for i in comp1 if i in comp2][0]
  prioritems.append(priorities[shared])

# puzzle 1: sum of the priorities of the shared items
print(sum(prioritems))

# puzzle 2: sum of the priorities of the badges
print(sum(badges))
