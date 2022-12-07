cleaning = open("day4/input.txt")

count = 0
count2 = 0
for line in cleaning:
  areas = [[int(i) for i in l.split('-')] for l in line.strip().split(',')]
  if areas[0][0] >= areas[1][0] and areas[0][1] <= areas[1][1]:
      count += 1
  elif areas[0][0] <= areas[1][0] and areas[0][1] >= areas[1][1]:
      count += 1
  # where is there overlap at all
  if areas[0][0] <= areas[1][0] and areas[0][1] >= areas[1][0]:
      count2 += 1
  elif areas[1][0] <= areas[0][0] and areas[1][1] >= areas[0][0]:
      count2 += 1
      
# Puzzle 1: count overlapping areas
print(count)

# Puzzle 2: count areas with any overlap
print(count2)
