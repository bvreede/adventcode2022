stacks = open("day5/input.txt")

# read the input to collect the crates
fromtop = 0
empty = 0
leveldict = {}
for line in stacks:
  if line.strip() == '':
    break
  fromtop += 1
  level = []
  splitline = (line.split(' '))
  for case in splitline:
    if case == '' or case == '\n':
      empty +=1
    else:
      empty = 0
    if empty == 4:
      level.append('[ ]')
      empty = 0
    elif empty == 0:
      level.append(case.strip())
  leveldict[fromtop] = level
    
# move them into a dictionary with lists that only register full crates
stackdict = {}
for stack in leveldict[fromtop]: # last level is the number of stacks
  stack_i = int(stack) -1
  crates = []
  for i in range(fromtop,0,-1):
    crate = leveldict[i][stack_i]
    if crate != '[ ]':
      crates.append(crate)
  stackdict[stack] = crates[1:]

stacks.close()


# read the instructions
instructions = open("day5/input.txt")

for line in instructions:
  line = line.split()
  try:
    if line[0] != 'move':
      continue
  except IndexError:
    continue
  num = line[1]
  source = line[3]
  dest = line[5]
  less = (int(num) + 1)*-1
  # new = stackdict[source][:less:-1] # puzzle 1
  new = stackdict[source][less+1::1] # puzzle 2
  stackdict[dest] = stackdict[dest] + new
  stackdict[source] = stackdict[source][:less+1]

puzzle1 = ''
for n in stackdict:
  print(n)
  print(stackdict[n])
  strip = stackdict[n][-1][1]
  puzzle1 += strip
  
print(puzzle1)
  

